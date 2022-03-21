from nltk.stem.snowball import SnowballStemmer
from nltk import pos_tag
from util import *

# Add your import statements here

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
stemmer = SnowballStemmer("english")


class InflectionReduction:

    def reduce(self, text):
        """
        Stemming
        Parameters
        ----------
        arg1 : list
                A list of lists where each sub-list a sequence of tokens
                representing a sentence
        Returns
        -------
        list
                A list of lists where each sub-list is a sequence of
                stemmed tokens representing a sentence
        """
        
        if isinstance(text, list):
            for i in range(len(text)):
                # for a list of tokens corresponding to a sentence
                for j in range(len(text[i])):
                    text[i][j] = stemmer.stem(
                        text[i][j])
                    # for word in the list of tokens:
                        # stem the word and replace the corresponding word in the input list
                    pass
            return text

        else:
            print("Warning.")
            return 0

    # Not used here but coded just in case needed in future
    def reduce_using_lemmatization(self, text):
        """
        Lemmatization
        Declared in case required later on.
        Parameters
        ----------
        arg1 : list
                A list of lists where each sub-list a sequence of tokens
                representing a sentence
        Returns
        -------
        list
                A list of lists where each sub-list is a sequence of
                stemmed/lemmatized tokens representing a sentence
        """
        if isinstance(text, list):
            for i in range(len(text)):
                pos_tags = pos_tag(text[i])
                # find the pos_tag for each word in a sentence
                for j in range(len(text[i])):
                    # convert the pos_tag to a format recognizable by the wordnet lemmatizer
                    pos = convert_to_wordnet_understandable_POS(
                        pos_tags[j][1])
                    text[i][j] = wordnet_lemmatizer.lemmatize(
                        text[i][j], pos=pos)
            return text

        else:
            print("Warning.")
            return 0