from google.cloud import firestore
from google.cloud.firestore_v1.document import DocumentSnapshot
import ContentHelper
#TODO Wrapper for 1cademy web api, need to wait for Iman to write backend code
# to be able to write this
#
# These are the functions I can think of for now, we may need more as time goes on
#  
#
#
db = None

def init_database():
    global db
    if not db:
        db = firestore.Client()

def get_nodes():
    nodes = db.collection(u'nodes')

    return [i.to_dict() for i in nodes.stream()]

#Accepts a 1CademyNode as a DocumentSnapshot and returns information as it would be expected by 
#the gensim Word2Vec model
#
#e.g. [['list', 'of', 'sentences'], ['another', 'sentence']]
#
# This is where node sanitizing and formatting will happen before being passed to the training model
def node_for_model(node: DocumentSnapshot):
    return ContentHelper.labeled_sentance_for_node(node)

def node_generator():
    nodes = list(db.collection(u'nodes').order_by('wiki').limit(1).stream())
    
    
    while len(nodes) > 0:
        wiki = nodes[0].to_dict()[u'wiki']
        print(wiki)
        yield node_for_model(nodes[0])
        nodes = list(db.collection(u'nodes').order_by('wiki').start_after({u'wiki': wiki}).limit(1).stream())


#TODO, find out the difference between reference and content nodes
#in the backend to be able to grab them seperately
def reference_generator():
    references = list(1)

    for reference in references:
        yield reference

#Todo, write implementation!
#Requires a summary with punctuation, acceptable for publishing
#as a string
def propose_node(proposeSummary):
    #1CademyApi.propose or whatever the REST call is
    pass

def propose_reference():
    pass

def get_references():
    pass

init_database()

if __name__ == '__main__':
    print(list(node_generator()))