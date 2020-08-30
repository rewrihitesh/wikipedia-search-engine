import re
import itertools
from array import array
from timeit import default_timer
from collections import defaultdict

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
					for (t,n) in zip(text,numbers):
						n=int(n)
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
		



def main():
	index=defaultdict(list)
	index=readIndex("/home/hitesh/sem3/IRE/wiki/phase1/index")

if __name__ == "__main__":
	start = default_timer()
	main()
	stop = default_timer()
	print ('\nTotal Time elasped in sec: ',stop - start)