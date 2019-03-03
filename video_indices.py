import webvtt
from nltk.tokenize import sent_tokenize, word_tokenize

"""
Input: 
Name of subtitle file - 1qy9xVEOI40_auto.en.vtt
summarized text file - 1qy9xVEOI40_sum.txt
tolerance is the difference (in seconds) between two sequential timestamp tuples that should be combined

Output: List of timestamp tuples (start, end) for the summarized video
"""
def video_indices(subtitle, text_summary, tolerance=0):
    text_summary = open(text_summary, "r").read()
    sents = [word_tokenize(s.lower()) for s in sent_tokenize(text_summary)]
    captions = webvtt.read(subtitle)
    cuttimes = []
    for sent in sents:
        beg = ' '.join(sent[:5])
        last = ' '.join(sent[-6:-1])
        for i, caption in enumerate(captions):
            captext = caption.text.replace("\n", " ")
            captext = filter_captext(captext)
            if beg in captext:
                start = caption.start
                for j, cap in enumerate(captions):
                    if i>j:
                        continue
                    captext = cap.text.replace("\n", " ")
                    captext = filter_captext(captext)
                    end = None
                    if last in captext:
                        end = caption.end
                        break
                if start and end:
                    timestamp = [start, end]
                    cuttimes.append([min(timestamp, key=time_for_one), max(timestamp, key=time_for_one)])
                break
    return cutttimes_filter(cuttimes, 10, 1000)

def tolerance_manager(cuttimes, tolerance):
    pstart=float("-inf")
    pend=float("-inf")
    cstart=0
    cend=0
    newcuttimes=[]
    flag=False
    for clip in cuttimes:
        cstart, cend = time_in_s(clip)
        if cstart-pend<=tolerance:
            flag=True
            newcuttimes.append([pstart, cend])
            pstart, pend=0,0
        else:
            newcuttimes.append([pstart, pend])
            pstart, pend = cstart, cend
    if pstart and pend:
        newcuttimes.append([pstart, pend])

    if flag==True:
        return tolerance_manager(newcuttimes, tolerance)
    return newcuttimes


def total_time(cuttimes):
    tot = 0
    for clip in cuttimes:
        s, e = time_in_s(clip)
        tot+= e-s
    return tot

def time_in_s(clip):
    start = clip[0].split(':')
    end = clip[1].split(':')
    s = 0
    e = 0
    for i in range(3):
        s+=float(start[i])*pow(60, 2-i)
        e+=float(end[i])*pow(60, 2-i)
    return s, e

def time_for_one(timestamp):
    timestamp = timestamp.split(':')
    a = 0
    for i in range(3):
        a+=float(timestamp[i])*pow(60, 2-i)
    return a

def cutttimes_filter(cuttimes, min_length=10, max_length=1000):
    new_cuttimes=[]
    for clip in cuttimes:
        s, e = time_in_s(clip)
        if e-s>min_length and e-s<max_length:
            new_cuttimes.append(clip)
    return new_cuttimes

def filter_captext(captext):
    apos = captext.find("'")
    if apos!=-1 and captext[apos+1]=='s':
        captext = captext[:apos] + captext[apos+2:]
        return filter_captext(captext)
    return captext

if __name__ == "__main__":
    cuttimes = video_indices("1qy9xVEOI40_auto.en.vtt","1qy9xVEOI40_sum.txt")
    print(cuttimes)
    count=0
    for clip in cuttimes:
        s, e = time_in_s(clip)
        if e-s<=0:
            count+=1
        print(e-s)
    print(count)
    print(total_time(cuttimes))
