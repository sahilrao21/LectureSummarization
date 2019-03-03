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
    chosen_sentences = summarizer(parser.document, model_utilities.summary_length(text))

    summary = ""
    for sentence_tuple in chosen_sentences:
        line = ""
        for word in sentence_tuple.words:
            line += word + " "
        summary += line

    return summary


url = "https://www.youtube.com/watch?v=1qy9xVEOI40"
vtt = dl_youtube.video_download(url, 22)[1]
file = puncuator.punctuate_transcript(vtt)

#with open("luhn_summary.txt", "w+") as luhn_summary_file:
#    luhn_summary_file.write(luhn_summarizer(file))
print(luhn_summarizer(file))