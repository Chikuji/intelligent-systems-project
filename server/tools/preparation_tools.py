import pickle

from instances.config import NLTK_STOPWORDS_PATH

class PreparationTools():

    def __init__(self):
        
        self.nltk_stop_words = pickle.load(open(NLTK_STOPWORDS_PATH, 'rb'))
        

    def create_text_feature(self, data):
        """
        Receives dictoinary of text columns, concatenate them, and remove stopwords.
        
        :param data: a dictionary.
        :param stop_words_list: a list of stop words.
        
        :returns: a string containing the concatenated string"""
        
        data = str(data['title']) + " " + str(data['query']) + " " + str(data['concatenated_tags'])

        data = ' '.join([word for word in data.split() if word not in (self.nltk_stop_words)])
        
        return data

    
    def filling_NAs(self):

        # even though it just an empty string, we'll keep this function in case
        ## we need to implement a different filling method in the future (just keeping the pipeline)

        return ''


