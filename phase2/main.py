from timeit import default_timer
from parser import wikihandler
import xml.sax as sax
import utility
def main():
	# setting path to indices
	utility.setIndexPath()
	utility.setStatPath()

	# parser=sax.make_parser()
	# handler = wikihandler()
	# parser.setFeature(sax.handler.feature_namespaces,0)
	# parser.setContentHandler(handler)
	# parser.parse("/home/hitesh/sem3/IRE/Project/large.xml")
	# parser.parse("/home/hitesh/sem3/IRE/wiki/phase2/large.xml")
	# parser.parse("/mnt/sdb1/phase2/data/0.xml") # 1
	# parser.parse("/mnt/sdb1/phase2/data/1.xml") # 2
	# parser.parse("/mnt/sdb1/phase2/data/29.xml") # 3
	for i in range(0,35):
		start = default_timer()
		parser=sax.make_parser()
		handler = wikihandler()
		parser.setFeature(sax.handler.feature_namespaces,0)
		parser.setContentHandler(handler)
		# this is the path to ur indices
		parser.parse("/mnt/sdb1/phase2/data/"+str(i)+".xml")
		stop = default_timer()
		print ('\nTime elasped in sec: ',stop - start)
		print('file no.:: ',str(i))
	
	#wrie index here 
	# handler.writeIndex(utility.getIndexPath()) # temp

if __name__ == "__main__":
	start = default_timer()
	main()
	stop = default_timer()
	print ('\nTotal Time elasped in sec: ',stop - start)
