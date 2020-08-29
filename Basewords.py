from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def baseword(text):  #assuming text is a list of words   
    ps = PorterStemmer()
    base = []

    for w in text:
        print(w, " : " , ps.stem(w))
        base.append(ps.stem(w))

    return base

if __name__ == "__main__":
    baseword(['programs', 'programming'])
