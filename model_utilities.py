from nltk.tokenize import sent_tokenize

def summary_length(text, n = 0.33):
    num_of_sentences = len(sent_tokenize(text))
    return int(n * num_of_sentences)
