from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

import dl_youtube
import puncuator
import model_utilities

def text_rank_summarizer(file):
    parser = PlaintextParser.from_file(file, Tokenizer("english"))
    summarizer = TextRankSummarizer()

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

with open("text_rank_summary.txt", "w+") as text_rank_summary_file:
    text_rank_summary_file.write(text_rank_summarizer(file))
