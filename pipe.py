import sys
import os
import json
import re
import string
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
import nltk

np.random.seed(400)
nltk.download('wordnet')


def perform_lemmatization(data):
    return stemmer.stem(WordNetLemmatizer().lemmatize(data, pos='v'))

def tokenize(content):
    tokens=[]
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS:
            tokens.append(perform_lemmatization(token))
    return result
content=[]

f=open("Office_Products_5.json","r")
lines=f.readlines()
special=",.:!()?[]&\"-*'"
for l in lines:
    json_line = json.loads(l)
    for x in json_line:
        s=str(json_line[x])
        if str(x)=="reviewText":
            content.append(tokenize(s))
	#print(x)
	#print(json_line[x])
	# f1.write(str(x).lower())
	# f1.write(" ")
	#s=str(json_line[x])
	#if str(x)=="reviewText":
	    #content.append(tokenize(s))
print(content)
f.close()


dictionary = gensim.corpora.Dictionary(content)

f=open("final_voc.txt","w")
count = 0
for k, v in dictionary.iteritems():
    f.write(k)
    f.write(" ")
    f.write(v)
    f.write("\n")
    print(k, v)
    count += 1
f.close()


bow_corpus = [dictionary.doc2bow(doc) for doc in content]

lda_model =  gensim.models.LdaMulticore(bow_corpus, 
                                   num_topics = 4, 
                                   id2word = dictionary,                                    
                                   passes = 10,
                                   workers = 8)
for idx, topic in lda_model.print_topics(-1):
    print("Topic: {} \nWords: {}".format(idx, topic ))
    print("\n")

test_string="I've had mine for 4 years now and use it almost daily.  Never had any problems with it even after a few drops to the carpeted floor.  Large easy to read keys with a nice feel, not too hard - not too soft.  Large easy to read display.  All in all, good calculator for everyday basic functions.";
test_list=[]
test_list.append(test_string)

bow_vector = dictionary.doc2bow(preprocess(test_list))

for index, score in sorted(lda_model[bow_vector], key=lambda tup: -1*tup[1]):
    print("Score: {}\t Topic: {}".format(score, lda_model.print_topic(index, 5)))
