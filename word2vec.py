import pandas as pd
from gensim.models import Word2Vec

def similar(text1,text2):
    model = vectorizeinput(text1)
    return(model.wv.similarity(text1,text2))
    
def vectorizeinput(text):
    df = pd.read_csv('/Users/s0p01cs/Downloads/Test.csv')
    df.head()
    #df['Title_Content'] = df['Title'] + " " + df['Content']
    df2 = df.apply(lambda x: ','.join(x.astype(str)), axis=1)
    df_clean = pd.DataFrame({'clean': df2})
    sent = [row.split(',') for row in df_clean['clean']]
    model = Word2Vec(sent, min_count=1,size= 50,workers=3, window =3, sg = 1)
    print(model.wv.most_similar(text)[0])
    return model

text = 'Computer Science'
#print (vectorizeinput(text))
#print (similar('Inductive Reasoning','Computer Science'))
