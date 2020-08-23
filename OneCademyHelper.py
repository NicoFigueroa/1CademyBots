from google.cloud import firestore

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
        print("db", db)

def get_nodes():
    nodes = db.collection(u'nodes')
    print(nodes)
    print(dir(nodes))
    return nodes

def propose_node():
    pass

def propose_reference():
    pass

def get_references():
    pass

init_database()