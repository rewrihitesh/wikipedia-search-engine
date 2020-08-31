import re
import itertools
from array import array
from timeit import default_timer
from collections import defaultdict
import sys
import utility
from nlp import preProcessor
from timeit import default_timer

index=defaultdict(list)

def readIndex(fileName):
	invertedIndex=defaultdict(list)
	with open(fileName,'r') as index:
		lines=index.readlines()
		for line in lines:
			token=line.split(';')
			token.pop()
			i=1
			dictkey=""
			for key in token:
				posting= array('I', [0,0,0,0,0,0,0])
				if(i==1):
					# it is key
					dictkey=key
					# invertedIndex[dictkey]=[]
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
			# print(dictkey)
			# print(invertedIndex[dictkey][0])
			# print(invertedIndex[dictkey][1])
			# print(invertedIndex[dictkey][2])
			# break
	return invertedIndex



def loadIndex():
	global index
	index=readIndex("/home/hitesh/sem3/IRE/wiki/phase1/inverted_index")

def parseQuery(query):
	pp=preProcessor()
	if ':' in query:
		fieldQuery(query,pp)
	else:
		plainQuery(query,pp)

def plainQuery(query,pp):
	global index
	tokens=query.split()
	for word in tokens:
		x=pp.tokenisStopWordsStemming(word,r'\d+|\w+')
		print(x[0],"::",index[x[0]])

def fieldQuery(tokens,pp):
	global index
	temp=re.findall(r'\w+',tokens)
	for t in temp:
		idx=0
		if(t=='d'):
			idx=0
		elif(t=='t'):
			idx=1
		elif(t=='i'):
			idx=2
		elif(t=='c'):
			idx=3
		elif(t=='r'):
			idx=4
		elif(t=='b'):
			idx=5
		elif(t=='e'):
			idx=6
		else:
			word=pp.tokenisStopWordsStemming(t)
			postingList=index[word[0]] # lis of arrays
			for posting in postingList:
				if(posting[idx]>0):
					print(word,' :: ',postingList)
					break



if __name__ == "__main__":

	start = default_timer()
	
	print("array[docID,title,infobox,category,references,body,externalLinks]")

	loadIndex()

	query=sys.argv[1]
	
	parseQuery(query)

	stop = default_timer()
	print ('\n Search Time in sec: ',stop - start)