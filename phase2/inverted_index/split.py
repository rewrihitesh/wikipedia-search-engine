import sys
import math
file = open("globalsort.txt","rt")

i=0

readbytes=0

for line in file:
	if(i==0 or readbytes>26214400):
		readbytes=0;
		file=open("temp/"+str(i),"w+")
		i+=1
	readbytes+=file.write(line)
	