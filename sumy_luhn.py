from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

import dl_youtube
import puncuator
import model_utilities

def luhn_summarizer(file):
    parser = PlaintextParser.from_file(file, Tokenizer("english"))
    summarizer = LuhnSummarizer()

    text = open(file, 'r').read()
    summary = summarizer(parser.document, model_utilities.summary_length(text))

    for sentence in summary:
        print(sentence)


url = "https://www.youtube.com/watch?v=1qy9xVEOI40"
vtt = dl_youtube.video_download(url, 22)[1]
file = puncuator.punctuate_transcript(vtt)

file.open("luhn_summary.txt", "w+")
file.write(luhn_summarizer(file))
file.close()
