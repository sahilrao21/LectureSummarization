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
    summary = summarizer(parser.document, model_utilities.summary_length(text))

    for sentence in summary:
        print(sentence)


url = "https://www.youtube.com/watch?v=1qy9xVEOI40"
vtt = dl_youtube.video_download(url, 22)[1]
file = puncuator.punctuate_transcript(vtt)

file.open("text_rank_summary.txt", "w+")
file.write(text_rank_summarizer(file))
file.close()
