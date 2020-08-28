from timeit import default_timer
from parser import wikihandler
import xml.sax as sax

def main():
	pass
	parser=sax.make_parser()
	handler = wikihandler()
	parser.setFeature(sax.handler.feature_namespaces,0)
	parser.setContentHandler(handler)
	parser.parse("/home/hitesh/sem3/IRE/Project/large.xml")
	print("tc:",handler.titleCount)

if __name__ == "__main__":
	start = default_timer()
	main()
	stop = default_timer()
	print (stop - start)
