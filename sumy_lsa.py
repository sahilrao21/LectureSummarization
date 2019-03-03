from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

import dl_youtube
import puncuator
import model_utilities

def lsa_summarizer(file):
    parser = PlaintextParser.from_file(file, Tokenizer("english"))
    summarizer = LsaSummarizer()

    text = open(file, 'r').read()
    chosen_sentences = summarizer(parser.document, model_utilities.summary_length(text))

    summary = ""
    for sentence_tuple in chosen_sentences:
        line = ""
        for i in range(len(sentence_tuple.words)):
            if i == len(sentence_tuple.words) - 1:
                line += sentence_tuple.words[i] + "."
            else:
                line += sentence_tuple.words[i] + " "
        summary += line + " "

    return summary


url = "https://www.youtube.com/watch?v=1qy9xVEOI40"
vtt = dl_youtube.video_download(url, 22)[1]
file = puncuator.punctuate_transcript(vtt)

with open("lsa_summary.txt", "w+") as lsa_summary_file:
    lsa_summary_file.write(lsa_summarizer(file))
