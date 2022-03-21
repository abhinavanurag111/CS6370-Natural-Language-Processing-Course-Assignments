from util import *
# Add your import statements here
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

class StopwordRemoval():

    def fromList(self, text):
        """
        Sentence Segmentation using the Punkt Tokenizer
        Parameters
        ----------
        arg1 : list
                A list of lists where each sub-list is a sequence of tokens
                representing a sentence
        Returns
        -------
        list
                A list of lists where each sub-list is a sequence of tokens
                representing a sentence with stopwords removed
        """
        for i in range(len(text)):
                tokens_without_stop_words = []
                # create an empty list for each tokenized sentence
                list_of_tokens = text[i]
                for word in list_of_tokens:
                        if word not in stop_words:
                                tokens_without_stop_words.append(word)
                text[i] = tokens_without_stop_words
        return text
