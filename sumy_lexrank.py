from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import dl_youtube
import puncuator

def sumy_lex(file):
    parser = PlaintextParser.from_file(file, Tokenizer("english"))
    summarizer = LexRankSummarizer()

    # Potential optimization
    summary = summarizer(parser.document, 40)

    for sentence in summary:
        print(sentence)


url = "https://www.youtube.com/watch?v=LERtLI2h_nQ"
vtt = dl_youtube.video_download(url, False, 22)[1]
file = puncuator.punctuate_transcript(vtt)
sumy_lex(file)