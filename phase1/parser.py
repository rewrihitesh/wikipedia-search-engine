import xml.sax
from nlp import preProcessor

class wikihandler(xml.sax.ContentHandler):
	def __init__(self):
		self.title=False
		self.text=False;
		
		self.bufText=""
		self.bufTitle=""

		self.titleCount=0
		self.pp=preProcessor()

	def startElement(self,tag,attrs):
		if(tag=="title"):
			self.title=True;
		elif(tag=="text"):
			self.text=True;
		

	def endElement(self,tag):
		if(tag=="title"):
			self.title=False;
			self.pp.processTitle(self.bufTitle)
			self.bufTitle=""
		elif(tag=="text"):
			self.text=False;
			self.pp.processText(self.bufText)
			self.bufText=""
	
	def characters(self,data):
		if self.title:
			self.bufTitle+=data
			# print(data," :: ",end=" ")
			self.titleCount+=1
		elif self.text:
			self.bufText+=data