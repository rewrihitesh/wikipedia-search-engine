from timeit import default_timer
from parser import wikihandler
import xml.sax as sax
import utility
def main():
	pass
	parser=sax.make_parser()
	handler = wikihandler()
	parser.setFeature(sax.handler.feature_namespaces,0)
	parser.setContentHandler(handler)
	parser.parse("/home/hitesh/sem3/IRE/Project/large.xml")
	# parser.parse("/home/hitesh/sem3/IRE/wiki/phase1/large.xml")
	curPath=utility.getCurrentPath()
	handler.writeIndex(curPath+'/inverted_index')

if __name__ == "__main__":
	start = default_timer()
	main()
	stop = default_timer()
	print ('\nTotal Time elasped in sec: ',stop - start)
