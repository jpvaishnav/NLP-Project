import sys
import os
import json
import re
import string
from collections import defaultdict
import matplotlib.pyplot as plt
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
# f=open("vocabulary.txt","w")
# for w in dic:
# 	f.write(w)
# 	f.write("\t")
# 	f.write(str(dic[w]))
# 	f.write("\n")
# f.close()
# reversed(sorted(dic.items(), key = lambda kv:(dic[1], dic[0])))
sorted_keys = sorted(dic, key=dic.get)
#print(sorted_keys)
sorted_dict = {}
f=open("zipf.txt","w")
f.write("word\tFrequency\tRank\tFrequency*Rank\n")
r=1
x=[]
y=[]
for w in reversed(sorted_keys):
	#print(w,dic[w])
	f.write(w)
	f.write("\t")
	f.write(str(dic[w]))
	if(dic[w]>=3000 and dic[w]<=9000):
		y.append(int(dic[w]))
	f.write("\t")
	f.write(str(r))
	if dic[w]>=3000 and dic[w]<=9000:
		x.append(r)
	k=(int(r)*dic[w])
	f.write("\t")
	f.write(str(k))
	f.write("\n")
	r+=1
f.close()
# for i in sorted_dict:
# 	print(i,sorted_dict[i])
plt.plot(x, y, label = "Zipf's law")
plt.xlabel('Rank')
# naming the y axis
plt.ylabel('Frequency')
# giving a title to my graph
plt.title("Zipf's law")


plt.legend()
  
# function to show the plot
plt.show()

