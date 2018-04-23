import unicodedata


def clean_word(word):
    """Returns the longest prefix of a word made of latin unicode characters."""
    for i, c in enumerate(word):
        if not unicodedata.name(c).startswith("LATIN"):
            return word[:i].lower()
    return word.lower()


def clean_words(words):
    """Cleans all words in a string."""
    return " ".join(map(clean_word, words.split()))
