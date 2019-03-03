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
        flag = True
        for i, caption in enumerate(captions):
            captext = caption.text.replace("\n", " ")
            captext = filter_captext(captext)
            if beg in captext:
                start = caption.start
                for caption in captions[i:]:
                    captext = caption.text.replace("\n", " ")
                    captext = filter_captext(captext)
                    if last in captext:
                        end = caption.end
                        break
                cuttimes.append([start, end])
                break


def tolerance_manager(cuttimes, tolerance):
    pass

def filter_captext(captext):
    apos = captext.find("'")
    if apos!=-1:
        captext = captext[:apos] + captext[apos+2:]
        return filter_captext(captext)
    return captext

if __name__ == "__main__":
    video_indices("1qy9xVEOI40_auto.en.vtt","1qy9xVEOI40_sum.txt")