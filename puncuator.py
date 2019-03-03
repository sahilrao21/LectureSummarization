from transcript_of_captions import generate_transcript
from requests import post


"""
Ensures that subtitle files are punctuated

Input:
Subtitle Filename

Output:
Trascript as a Text File including punctuation, in the format video_id.txt
Returns name of the text file.

Source: ML Model from the Institute of Cybernetics of Tut
"""

def punctuate_transcript(subtitle):
    i = subtitle.find(".en.vtt")
    name = subtitle[:i]
    t = generate_transcript(subtitle)
    if "auto" not in subtitle:
        open(name+".txt", "w").write(t)
        return name+".txt"
    else:
        r = post('http://bark.phon.ioc.ee/punctuator', data={'text': t})
        open(name[:-5]+".txt", "w").write(r.text)
        return name[:-5]+".txt"

if __name__=="__main__":
    subtitle = "fQgupEKPsbc.en.vtt"
    punctuate_transcript(subtitle)
