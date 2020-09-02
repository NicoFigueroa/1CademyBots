from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import gensim
import word2vec

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
  filtered_sentence = [w for w in word_tokens if not w in stop_words]
  
  return filtered_sentence

def compare_vectors():
    pass

def vectorize():
    pass