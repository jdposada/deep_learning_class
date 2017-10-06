import os
from nltk import sent_tokenize
from nltk import word_tokenize

class SentenceIterator(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for sent in sent_tokenize(open(os.path.join(self.dirname, fname), 'r')):
                yield word_tokenize(sent)
