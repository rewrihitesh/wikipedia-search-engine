from collections import defaultdict

class invertedIndex():
	def __init__(self):
		self.index=defaultdict(list)
		self.globalKeySet=set()
		pass

	def makeDict(self,tokens):
		index=defaultdict(int)
		for token in tokens:
			self.globalKeySet.add(token)
			index[token]+=1
		return index

	def buildIndex(docID,titleTokens,infoboxTokens,
		categoryTokens,referencesTokens,bodyTokens,
		externalLinksTokens):

		titleDict=self.makeDict(titleTokens)
		infoboxDict=self.makeDict(infoboxTokens)
		categoryDict=self.makeDict(categoryTokens)
		referencesDict=self.makeDict(referencesTokens)
		bodyDict=self.makeDict(bodyTokens)
		externalLinksDict=self.makeDict(externalLinksTokens)

		for token in self.globalKeySet:
			posting=[docID,0,0,0,0,0,0]
			if(token in titleDict):
				posting[1]=titleDict[token]
			
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

			self.index[token].append(posting)




	def writeIndex():
		pass

	def readIndex():
		pass