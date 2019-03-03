from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import dl_youtube
import puncuator
import model_utilities

def lex_rank_summarizer(file, props=0.40):
    parser = PlaintextParser.from_file(file, Tokenizer("english"))
    summarizer = LexRankSummarizer()

    text = open(file, 'r').read()
    chosen_sentences = summarizer(parser.document, model_utilities.summary_length(text, props))

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


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=1qy9xVEOI40"
    vtt = dl_youtube.video_download(url, 22)[1]
    file = puncuator.punctuate_transcript(vtt)
    with open(file[:-4]+"_sum.txt", "w+") as lex_rank_summary_file:
        lex_rank_summary_file.write(lex_rank_summarizer(file))
