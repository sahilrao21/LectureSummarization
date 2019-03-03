from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import dl_youtube
import puncuator
import model_utilities

def lex_rank_summarizer(file):
    parser = PlaintextParser.from_file(file, Tokenizer("english"))
    summarizer = LexRankSummarizer()

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

print("vtt: ")
print(PlaintextParser.from_file(vtt, Tokenizer("english")))
print("normal file: ")

with open("lex_rank_summary.txt", "w+") as lex_rank_summary_file:
   lex_rank_summary_file.write(lex_rank_summarizer(file))
print("normal file: ")
print(lex_rank_summarizer(file))
