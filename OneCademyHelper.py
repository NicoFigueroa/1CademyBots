from google.cloud import firebase

#TODO Wrapper for 1cademy web api, need to wait for Iman to write backend code
# to be able to write this
#
# These are the functions I can think of for now, we may need more as time goes on
#  
#
#

def init_database():
    global db
    if not db:
        db = firebase.Client()

def get_nodes():
    return db.collection(u'nodes').get()

def propose_node():
    pass

def propose_reference():
    pass

def get_references():
    pass

