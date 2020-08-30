from collections import defaultdict
import pickle
from array import array
from enum import Enum
from utility import progress
class idx(Enum):
	ID=0
	TITLE=1
	INFOBOX=2
	CATEGORY=3
	REFERECES=4
	BODY=5
	EXTERNALlINKS=6

class invertedIndex():
	def __init__(self):
		self.index=defaultdict(list)
		self.globalKeySet=set()
		self.totalInvertedTokens=0
		self.totalTokens=0

	def makeDict(self,tokens):
		index=defaultdict(int)
		for token in tokens:
			self.globalKeySet.add(token)
			index[token]+=1
			self.totalTokens+=1
		return index

	def buildIndex(self,docID,titleTokens,infoboxTokens,
		categoryTokens,referencesTokens,bodyTokens,
		externalLinksTokens):

		titleDict=self.makeDict(titleTokens)
		infoboxDict=self.makeDict(infoboxTokens)
		categoryDict=self.makeDict(categoryTokens)
		referencesDict=self.makeDict(referencesTokens)
		bodyDict=self.makeDict(bodyTokens)
		externalLinksDict=self.makeDict(externalLinksTokens)

		for token in self.globalKeySet:
			posting= array('I', [0,0,0,0,0,0,0])
			posting[0] =int(docID)
			# print(type(posting[0]))

			if(token in titleDict):
				posting[1]=titleDict[token]
				# print(type(titleDict[token]))
			
			if(token in infoboxDict):
				posting[2]=infoboxDict[token]

			if(token in categoryDict):
				posting[3]=categoryDict[token]

			if(token in referencesDict):
				posting[4]=referencesDict[token]

			if(token in bodyDict):
				posting[5]=bodyDict[token]

			if(token in externalLinksDict):
				posting[6]=externalLinksDict[token]

			# print(token," :: ",posting)
			self.index[token].append(posting)

		self.globalKeySet.clear()

	################# PICKLE AS DUMP

	# def writeIndex(self,fileName):
	# 	print("totalInvertedTokens::", self.totalInvertedTokens)
	# 	with open(fileName, 'wb') as index:
	# 		pickle.dump(self.index, index, protocol=pickle.HIGHEST_PROTOCOL)

	################ CSV AS DUMP

	# def writeIndex(self,fileName):
	# 	print("totalInvertedTokens::", self.totalInvertedTokens)
	# 	file=open(fileName,'w+')
	# 	for key in self.index:
	# 		file.write(key)
	# 		file.write(',')
	# 		for element in self.index[key]:
	# 			for i in element:
	# 				file.write(str(i))
	# 				file.write(',')
	# 		file.write('\n')

	def writeIndex(self,fileName):
		self.totalInvertedTokens=len(self.index)
		print("totalInvertedTokens::", self.totalInvertedTokens)
		
		import os
		
		curPath = os.getcwd()
		statFile=open(curPath+'/inverted_stat.txt','a+')
		statFile.write("Total Inverted Tokens :"+str(self.totalInvertedTokens)+'\n')
		
		indexSize=len(self.index)
		j=0
		file=open(fileName,'w+')
		for key in self.index:
			file.write(key)
			file.write(';')
			for element in self.index[key]:
				for i in range(0,6):
					if(i==0 and element[i]!=0):
						file.write('d'+str(element[i]))
					elif(i==1 and element[i]!=0):
						file.write('t'+str(element[i]))
					elif(i==2 and element[i]!=0):
						file.write('i'+str(element[i]))
					elif(i==3 and element[i]!=0):
						file.write('c'+str(element[i]))
					elif(i==4 and element[i]!=0):
						file.write('r'+str(element[i]))
					elif(i==5 and element[i]!=0):
						file.write('b'+str(element[i]))
					elif(i==6 and element[i]!=0):
						file.write('e'+str(element[i]))
				file.write(';')
			file.write('\n')
			progress(j,indexSize,'writing index!!')
			j+=1


	def readIndex(self,fileName):
		with open(fileName, 'rb') as index:
			self.index = pickle.load(index)