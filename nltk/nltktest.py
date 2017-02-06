from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


a = "Hello Mr. Perera, how do you do. Today is such a lovely day. Nice hat!"

print(word_tokenize(a))
print(sent_tokenize(a))

for w in word_tokenize(a):
    if w not in stopwords.words():
        print PorterStemmer().stem(w)