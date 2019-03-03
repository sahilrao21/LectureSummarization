from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import dl_youtube
import transcript_of_captions


def sumy_lex(inp):
    file = inp
    parser = PlaintextParser.from_file("transcript3.txt", Tokenizer("english"))
    summarizer = LexRankSummarizer()

    summary = summarizer(parser.document, 10)

    for sentence in summary:
        print(sentence)


urll = "https://www.youtube.com/watch?v=svW3I0cqfpw"
vttt = dl_youtube.video_download(urll, 22)
trans = transcript_of_captions.generate_transcript(vttt)
# file = transcript_of_captions.populate_file(trans)
summary = sumy_lex(trans)

print(summary)

