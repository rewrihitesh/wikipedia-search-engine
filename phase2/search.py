import re
import itertools
from array import array
from collections import defaultdict
import sys
import utility
from nlp import preProcessor
from timeit import default_timer

def readIndex(fileName,keyword):
	invertedIndex=defaultdict(list)
	with open(fileName,'r') as index:
		lines=index.readlines()
		for line in lines:
			xy=line.split(';',1)
			if(xy[0]==keyword):
				token=line.split(';')
				print(token[0])
				token.pop()
				i=1
				j=0
				dictkey=""
				for key in token:
					posting= array('I', [0,0,0,0,0,0,0])
					if(i==1):
						# it is key
						dictkey=key
						# invertedIndex[dictkey]=[posting]*(len(token)-1)
						i+=1
					else:	
						regex=r'[a-z]+'
						text=re.findall(regex,key)
						numbers=re.findall(r'\d+',key)
						for (t,x) in zip(text,numbers):
							n=int(x)
							if(t=='d'):
								posting[0]=n
							elif(t=='t'):
								posting[1]=n
							elif(t=='i'):
								posting[2]=n
							elif(t=='c'):
								posting[3]=n
							elif(t=='r'):
								posting[4]=n
							elif(t=='b'):
								posting[5]=n
							elif(t=='e'):
								posting[6]=n

						invertedIndex[dictkey].append(posting)
						# invertedIndex[dictkey][j]=posting
						# print(invertedIndex[dictkey][j],end=" ")
						j+=1
				# print(dictkey)
				# print(invertedIndex[dictkey][0])
				# print(invertedIndex[dictkey][1])
				# print(invertedIndex[dictkey][2])
				# break
	return invertedIndex



