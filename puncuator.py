from transcript_of_captions import generate_transcript
from requests import post

def punctuate_transcript(subtitle):
    i = subtitle.find(".en.vtt")
    name = subtitle[:i]
    t = generate_transcript(subtitle)
    if "auto" not in subtitle:
        open(name, "w").write(t)
        return t
    else:
        r = post('http://bark.phon.ioc.ee/punctuator', data={'text': t})
        open(name[:-5]+".txt", "w").write(r.text)

if __name__=="__main__":
    subtitle = "zbf3ILq9IJs_auto.en.vtt"
    punctuate_transcript(subtitle)