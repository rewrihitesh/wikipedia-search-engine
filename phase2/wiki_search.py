# imports 
from bisect import bisect
from math import log
from search import *

# files

totalDocs=1

def loadTotalDocs(docTitleDocsPath="inverted_index/totalDocs"):
	global totalDocs
	file=open(docTitleDocsPath,"r")
	line=file.readline()
	totalDocs=int(line)

def loadTitle(docTitlePath="inverted_index/doctitle.txt"):
	titleDic=defaultdict(str)
	title=open(docTitlePath,"r")
	lines=title.readlines()
	for line in lines:
		parts=line.split(';')
		titleDic[int(parts[0])]=parts[1]
	return titleDic

def loadSecondaryIndex(docSecondaryIndexPath="inverted_index/secondryIndex"):
	name=[]
	index=[]
	secondaryIndexFile=open(docSecondaryIndexPath,"r")
	lines=secondaryIndexFile.readlines()
	for line in lines:
		parts=line.split(';')
		name.append(parts[0])
		index.append(parts[1].rstrip('\n'))
	return name,index

def loadTitleSecondaryIndex(docSecondaryIndexPath="inverted_index/secondryTitleIndex"):
	name=[]
	index=[]
	secondaryIndexFile=open(docSecondaryIndexPath,"r")
	lines=secondaryIndexFile.readlines()
	for line in lines:
		parts=line.split(';')
		name.append(int(parts[0]))
		index.append(parts[1].rstrip('\n'))
	return name,index

def loadInvertedIndex(keyword,fileName,indexPath="inverted_index/temp/"):
	filePath=indexPath+fileName
	indexFile=open(filePath,"r")
	# it returns index dictionary containing list of arrays
	return readIndex(filePath,keyword)
def parseQuery(query,pp):
	if ':' in query:
		return fieldQuery(query,pp)
	else:
		return plainQuery(query,pp)

def plainQuery(query,pp):
	tokens=query.split()
	listOfStemmed=[]
	for word in tokens:
		x=pp.tokenisStopWordsStemming(word)
		if(len(x)>0):
			listOfStemmed.append([x[0],[0,9,4,1,1,1,1]])
	return listOfStemmed

def fieldQuery(tokens,pp):
	global index
	temp=re.findall(r'\d+|\w+',tokens)
	# print(temp)
	listOfStemmed=[]
	weight=7*[1]
	for t in temp:
		idx=0
		if(t=='d'):
			idx=0
		elif(t=='t'):
			idx=1
			weight[idx]+=12
		elif(t=='i'):
			idx=2
			weight[idx]+=5
		elif(t=='c'):
			idx=3
			weight[idx]+=1
		elif(t=='r'):
			idx=4
			weight[idx]+=1
		elif(t=='b'):
			idx=5
			weight[idx]+=2
		elif(t=='e'):
			idx=6
			weight[idx]+=1
		else:
			word=pp.tokenisStopWordsStemming(t,r'\d+|\w+')
			if(len(word)>0):
				listOfStemmed.append([word[0],weight])
	return listOfStemmed
	
def tfidf(postingList,weights=[0,2,1.5,0.5,0.5,0.7,0.5]):
	global totalDocs
	# print(weights)
	# id, title, infobox, cat , ref, body , links
	weightdDoc=[]
	itemFrequency=7*[1]
	idfFrequency=7*[0]
	totalTermDocs=len(postingList)
	if(totalTermDocs==0):
		weightdDoc.append([0,0])
		return weightdDoc

	# idf=log(totalDocs/totalTermDocs)

	# calculate tf according to fields

	for posting in postingList:
		for i in range(1,7):
			if(posting[i] != 0):
				itemFrequency[i]+=1
	
	# idf according to fields

	for i in range(1,7):
		idfFrequency[i]=log(totalDocs/itemFrequency[i])

	for posting in postingList:
		freqSum=0
		tfSum=0
		td_idf=0
		for i in range(1,7):
			td_idf+=log(1+posting[i])*idfFrequency[i]*weights[i]

		weightdDoc.append([td_idf,posting[0]])

	return weightdDoc

def intersection(listOfDicionary):
	intersectionDict=defaultdict(float)
	for i in listOfDicionary:
		wlist=tfidf(i[0],i[1])
		# print(wlist)
		for j in wlist:
			intersectionDict[j[1]]+=j[0]
	resultList=[]
	for k,v in sorted(intersectionDict.items(),key=lambda kv:(kv[1], kv[0]),reverse=True):
		resultList.append(k)
	return resultList

def main():
	# titleDict=loadTitle()
	titleFileHead,titleFileName=loadTitleSecondaryIndex()
	loadTotalDocs()
	indexFileHead,indexFileName=loadSecondaryIndex()
	pp=preProcessor()
	# query parse here
	pathToQuaries="quaries.txt"
	pathToOuputQuaries="quaries_op.txt"
	quaryOutputFile=open(pathToOuputQuaries,"w+")
	quaryFile=open(pathToQuaries,"r")
	lines=quaryFile.readlines()
	for line in lines:

		start = default_timer()
		
		split=line.split(',',1)
		k=int(split[0])
		query=split[1]
	# completed
		# query="t:apple iphone os i: mac"
		parsedQuery=parseQuery(query,pp)
		listOfDicionary=[]
		for idx,i in enumerate(parsedQuery):
			y=bisect(indexFileHead, i[0])
			# print(indexFileHead[y])
			indexDict=loadInvertedIndex(i[0],fileName=str(y-1))
			listOfDicionary.append([indexDict[i[0]],i[1]])
		weightdDoc=intersection(listOfDicionary)
		for i in range(min(k,len(weightdDoc))):
			docid=weightdDoc[i]
			z=bisect(titleFileHead, int(docid))
			titleDict=loadTitle("inverted_index/title/"+str(z-1))
			print(titleDict[docid])
			quaryOutputFile.write(str(docid)+' ')
			quaryOutputFile.write(titleDict[docid])
		stop = default_timer()
		quaryOutputFile.write(str((stop - start))+'\n\n')

if __name__ == "__main__":
	start = default_timer()
	main()
	stop = default_timer()
	print ('\nTotal Time elasped in sec: ',stop - start)
