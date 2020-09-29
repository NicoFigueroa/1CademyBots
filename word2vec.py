import pandas as pd
from gensim.models import Word2Vec, Doc2Vec

import OneCademyHelper


#TODO Implement vector comparrison between two paragraphs, 
#Doc2Vec may be the solution here
def compare_nodes(wiki_summary, node):
    return False


#TODO implement comparrison of references somehow,
#probably not with vectors but we need to come up with a 
#comparrison method
#
#Maybe something like title similarity and author overlap? 
def compare_references(wikiReference, existingReference):
    return False

def similar(text1,text2):
    return(model.wv.similarity(text1,text2))

def vectorizeinput(nodes):
    model = Word2Vec()

if __name__ == '__main__':
    model = Doc2Vec(alpha=0.025, min_alpha=0.025)
    model.build_vocab(OneCademyHelper.node_generator())
    
    for epoch in range(5):
        model.train(OneCademyHelper.node_generator(), total_examples=model.corpus_count, epochs=model.epochs)
        print(epoch)

    model.save('C:\\Users\\figue\\Documents\model.doc2vec')
    print(model.wv.similar_by_word("inteligent"))
    

    #print (vectorizeinput(text))
    #print (similar('Inductive Reasoning','Computer Science'))
