from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import dl_youtube
import puncuator

def sumy_lex(file):
    parser = PlaintextParser.from_file(file, Tokenizer("english"))
    summarizer = LexRankSummarizer()

    # Potential optimization
    text = open(file, 'r').read()
    summary = summarizer(parser.document, summary_length(text))

    for sentence in summary:
        print(sentence)


url = "https://www.youtube.com/watch?v=1qy9xVEOI40"
vtt = dl_youtube.video_download(url, 22)[1]

file = puncuator.punctuate_transcript(vtt)
#punctuate_transcript("asdasdsad.env.vtt")

#file = transcript_of_captions.populate_file(trans)

sumy_lex(file)