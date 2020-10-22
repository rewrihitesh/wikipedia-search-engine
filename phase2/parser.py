import xml.sax
from nlp import preProcessor
from invertedindex import invertedIndex
import utility


class wikihandler(xml.sax.ContentHandler):
	def __init__(self):
		self.page=False
		self.id=False
		self.firstID=True
		self.title=False
		self.text=False;
		
		self.bufID=""
		self.bufTitle=""
		self.bufText=""

		self.pageCount=0;
		self.pp=preProcessor()
		self.invertedIndex=invertedIndex()

	def startElement(self,tag,attrs):
		if(tag=="page"):
			self.page=True;
		elif(tag=="id" and self.firstID):
			self.id=True;
			self.firstID=False;
		elif(tag=="title"):
			self.title=True;
		elif(tag=="text"):
			self.text=True;
		

	def endElement(self,tag):
		if(tag=="page"):
			self.pageCount+=1
			# utility.progress(self.pageCount, total, status='Creating Index!!')

			# print(self.bufID)
			# print(self.bufTitle)
			# print(self.bufText)

			self.id=False
			self.firstID=True


			## build you index here page by page
			
			titleTokens=self.pp.processTitle(self.bufTitle)
			infoboxTokens,catgoriesTokens,referencesTokens,bodyTokens,externalLinksTokens=self.pp.processText(self.bufText)

			self.invertedIndex.buildIndex(self.bufID,titleTokens,
				infoboxTokens,catgoriesTokens,referencesTokens,
				bodyTokens,externalLinksTokens);

			# create a secondry index which will have buftile corresponding to id
			# filename will be doctitle.txt
			doctitleFile=open("inverted_index"+"/doctitle.txt","a+")
			doctitleFile.write(self.bufID+';'+self.bufTitle+'\n')
			# end of doc id title
			self.bufID=""
			self.bufTitle=""
			self.bufText=""

			# it is temporary

			if(self.pageCount%25000==0):
				print(self.pageCount, self.pp.totalTokens)
				self.invertedIndex.writeIndex("temporary")
				self.invertedIndex.index.clear()
				self.pp.dynamicStemming.clear()


		elif(tag=="id"):
			self.id=False
		if(tag=="title"):
			self.title=False;
		elif(tag=="text"):
			self.text=False;
		elif(tag=="mediawiki"):
			print("\nTotal Tokens :",self.pp.totalTokens)
			statFile=open(utility.getStatPath(),'a+')
			print("inverted_stat.txt path :",utility.getIndexPath())
			statFile.write("Total Tokens :"+str(self.pp.totalTokens)+'\n')
			statFile.close()
			self.invertedIndex.writeIndex("temporary")
			self.invertedIndex.index.clear()
			self.pp.dynamicStemming.clear()
	
	def characters(self,data):
		if(self.id):
			self.bufID+=data
		elif(self.title):
			self.bufTitle+=data
		elif(self.text):
			self.bufText+=data

	def writeIndex(self,fileName):
		self.invertedIndex.writeIndex(fileName)

	def readIndex(self,fileName):
		pass
