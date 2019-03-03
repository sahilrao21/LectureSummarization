from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
import dl_youtube
import puncuator

def gem_sim(file):
    parser = PlaintextParser.from_file(file, Tokenizer("english"))
    print(parser)

url = "https://www.youtube.com/watch?v=LERtLI2h_nQ"
vtt = dl_youtube.video_download(url, False, 22)[1]
file = puncuator.punctuate_transcript(vtt)
gem_sim(file)