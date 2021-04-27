import sys
import os
import json
import re
import string
from collections import defaultdict

f=open("zipf.txt","r")

lines=f.readlines()

words=[]
i=0
for l in lines:
	if i==0:
		i+=1
		continue
	List=l.split()
	k=int(List[3])
	if k>=1120000 and k<=1200000:
		words.append(str(List[0]))
print(words)