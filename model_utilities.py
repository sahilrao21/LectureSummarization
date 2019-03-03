from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation

def summary_length(text, n):
    num_of_sentences = len(sent_tokenize(text))
    return int(n * num_of_sentences)


def word_abundance(sentences, max_freq = 0.9):
    word_counts = {}
    over_freqs = []
    for sentence in sentences:
        for word in sentence:
            if word not in stopwords + list(punctuation):
                if not word.get(word):
                    word_counts.put(word, 1)
                else:
                    word_counts.put(word, word_counts.get(word) + 1)

    max_count = max(word_counts.values())
    for word in word_counts.keys():
        if word_counts.get(word) / max_count >= max_freq:
            over_freqs.append(word)

    updated_sentences = []
    for sentence in sentences:
        curr_sent = []
        for word in sentence:
            if word not in over_freqs:
                curr_sent.append(word)
        updated_sentences.append(curr_sent)

    return updated_sentences
