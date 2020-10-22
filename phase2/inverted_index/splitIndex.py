import sys
import math
file = open("docTitle.txt","r")

lines = file.readlines()

print(len(lines))
maxLines=10000
print(math.ceil(len(lines)/maxLines))
for i,line in enumerate(lines):
	if(i%maxLines==0):
		file=open("title/"+str(i//maxLines),"w+")
	file.write(line)
	