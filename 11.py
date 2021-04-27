import spacy
import sys
import os
import json
import re
import string

f1=open("dictionary.txt","w")
#open the json file and read line by line
f=open("Office_Products_5.json","r")
lines=f.readlines()
special=",.:!()?[]&\"-*'"
for l in lines:
	json_line = json.loads(l)
	for x in json_line:
		#print(x)
		#print(json_line[x])
		f1.write(str(x).lower())
		f1.write(" ")
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


