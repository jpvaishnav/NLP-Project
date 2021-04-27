
import sys
import os
import json
import re
import string
from collections import defaultdict
f=open("dictionary.txt","r")
lines=f.readlines()
cnt=1
dic=defaultdict(int)
for l in lines:
	List=l.split()
	for word in List:
		cnt+=1
		dic[word]+=1
f.close()
print("Size of vocabulary: ",cnt)
f=open("vocabulary.txt","w")
for w in dic:
	f.write(w)
	f.write("\t")
	f.write(str(dic[w]))
	f.write("\n")
f.close()

