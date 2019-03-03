from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import dl_youtube
import transcript_of_captions


def sumy_lex(file):
    parser = PlaintextParser.from_file(file, Tokenizer("english"))
    summarizer = LexRankSummarizer()

    # Potential optimization
    summary = summarizer(parser.document, 5)

    for sentence in summary:
        print(sentence)


url = "https://www.youtube.com/watch?v=svW3I0cqfpw"
vtt = dl_youtube.video_download(url, 22)
trans = transcript_of_captions.generate_transcript(vtt)
file = transcript_of_captions.populate_file(trans)

sumy_lex(file)