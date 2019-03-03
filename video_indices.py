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
    coptions = webvtt.read(subtitle)
    cuttimes = []
    for sent in sents[-5:]:
        beg = ' '.join(sent[:3])
        last = ' '.join(sent[-4:-1])
        for i, caption in enumerate(captions):
            captext = caption.text.replace("\n", " ")
            captext = filter_captext(captext)
            if beg in captext:
                start = caption.start
                break

        for coption in coptions:
            captext = coption.text.replace("\n", " ")
            captext = filter_captext(captext)
            if last in captext:
                s, e = time_in_s([start, coption.end])
                if e-s>0:
                    end = coption.end
                    break
        cuttimes.append([start, end])
        break

    return cuttimes


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
            pstart, pend=0
        else:
            newcuttimes.append([pstart, pend])
            pstart, pend = cstart, cend
    if pstart and pend:
        newcuttimes.append()

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

    return cuttimes
    # for caption in webvtt.read(subtitle)[:100]:
    #     print(caption.start)
    #     print(caption.text)

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
# if __name__ == "__main__":
#     video_indices("1qy9xVEOI40_auto.en.vtt","1qy9xVEOI40_sum.txt")
