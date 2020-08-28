import xml.sax
from nlp import preProcessor

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

		self.titleCount=0
		self.pp=preProcessor()

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
			self.firstID=False
			self.bufID=""
			
		elif(tag=="id"):
			self.id=False
		if(tag=="title"):
			self.title=False;
			self.pp.processTitle(self.bufTitle)
			self.bufTitle=""
		elif(tag=="text"):
			self.text=False;
			self.pp.processText(self.bufText)
			self.bufText=""
	
	def characters(self,data):
		if(self.id):
			self.bufID+=data
		elif(self.title):
			self.bufTitle+=data
			# print(data," :: ",end=" ")
			self.titleCount+=1
		elif(self.text):
			self.bufText+=data