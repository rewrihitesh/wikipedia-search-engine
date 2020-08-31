import xml.sax
from nlp import preProcessor
from invertedindex import invertedIndex
from utility import progress


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
			total = 19797
			
			progress(self.pageCount, total, status='Creating Index!!')
			# if(self.pageCount%1000==0 or self.pageCount>19600 ):
			# 	print(self.pageCount, self.pp.totalTokens)
			
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

			self.bufID=""
			self.bufTitle=""
			self.bufText=""

		elif(tag=="id"):
			self.id=False
		if(tag=="title"):
			self.title=False;
		elif(tag=="text"):
			self.text=False;
		elif(tag=="mediawiki"):
			print("\nTotal Tokens :",self.pp.totalTokens)
			statFile=open(utility.getIndexPath(),'w+')
			print("inverted_stat.txt path :",utility.getIndexPath())
			statFile.write("Total Tokens :"+str(self.pp.totalTokens)+'\n')
	
			statFile.close()
	
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
