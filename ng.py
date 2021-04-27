import spacy
import sys
import os
import json
import re
import string
from collections import defaultdict
import matplotlib.pyplot as plt
f1=open("review.txt","w")
#open the json file and read line by line
f=open("Office_Products_5.json","r")
lines=f.readlines()
special=",.:!()?[]&\"-*'"
for l in lines:
	json_line = json.loads(l)
	for x in json_line:
		#print(x)
		#print(json_line[x])
		if str(x)=="reviewText" or str(x)=="summary":
			# f1.write(str(x).lower())
			# f1.write(" ")
			s=str(json_line[x])
			#print("string is: ",s)
			for c in s:
				if (c in special) == False:
					f1.write(str(c).lower())
					#print("c written: ",c)
			#f1.write(s)
			f1.write(" ")

f.close()
f1.close()

#2g starts here
# f=open("review.txt","r")
# f1=open("2g.txt","w")
# lines=f.readlines()
# cnt=1
# dic=defaultdict(int)
# for l in lines:
# 	List=l.split()
# 	for i in range(len(List)-1):
# 		s=List[i]+" "+List[i+1]
# 		dic[s]+=1
# 		#print(s,dic[s])
# f.close()
# sorted_keys = sorted(dic, key=dic.get)
# r=1
# for w in reversed(sorted_keys):
# 	#print(w,dic[w])
# 	f1.write(w)
# 	f1.write("\t")
# 	f1.write(str(dic[w]))
# 	f1.write("\t")
# 	f1.write(str(r))
# 	f1.write("\n")
# 	r+=1
# f1.close()

#3g starts here
# f=open("review.txt","r")
# f1=open("3g.txt","w")
# lines=f.readlines()
# cnt=1
# dic=defaultdict(int)
# for l in lines:
# 	List=l.split()
# 	for i in range(len(List)-2):
# 		s=List[i]+" "+List[i+1]+" "+List[i+2]
# 		dic[s]+=1
# 		#print(s,dic[s])
# f.close()
# sorted_keys = sorted(dic, key=dic.get)
# r=1
# for w in reversed(sorted_keys):
# 	#print(w,dic[w])
# 	f1.write(w)
# 	f1.write("\t")
# 	f1.write(str(dic[w]))
# 	f1.write("\t")
# 	f1.write(str(r))
# 	f1.write("\n")
# 	r+=1
# f1.close()

#4g starts here
f=open("review.txt","r")
f1=open("4g.txt","w")
lines=f.readlines()
cnt=1
dic=defaultdict(int)
for l in lines:
	List=l.split()
	for i in range(len(List)-3):
		s=List[i]+" "+List[i+1]+" "+List[i+2]+" "+List[i+3]
		dic[s]+=1
		#print(s,dic[s])
f.close()
sorted_keys = sorted(dic, key=dic.get)
r=1
for w in reversed(sorted_keys):
	#print(w,dic[w])
	f1.write(w)
	f1.write("\t")
	f1.write(str(dic[w]))
	f1.write("\t")
	f1.write(str(r))
	f1.write("\n")
	r+=1
f1.close()