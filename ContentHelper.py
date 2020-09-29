from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import gensim
import word2vec
from gensim.models.doc2vec import TaggedDocument
#TODO module to vectorize and compare content between 1cademy nodes and wikipedia articles 
# to determine if the node already exists in 1cademy
# 
# We may need more or different functions, this is just initial thoughts to try and 
# find the right direction to progress in
#  

# Python module containing word2vec, https://stackabuse.com/implementing-word2vec-with-gensim-library-in-python/


#TODO takes a wiki article summary as input and removes all numbers, 
# changes uppercase to lower and removes references

def sanitize(text):
  stop_words = set(stopwords.words('english'))
  word_tokens = word_tokenize(text)
  filtered_sentence = [w.lower() for w in word_tokens if not w in stop_words]
  
  return filtered_sentence

def get_unique_identifier_for_node(node):
    return node.to_dict()['wiki']

def labeled_sentance_for_node(node):
    node = node.to_dict()
    
    document = TaggedDocument(words=node['content'].split(), tags=[node['wiki']])

    return document