import heapq as pq

noOfFiles=409

fname=list(range(0,noOfFiles))

files=[open(str(i),"r") for i in fname]
heaplist=[]
count=noOfFiles
golbalfile= open("globalsort.txt","w+")

for i in fname:
	if(files[i].closed is False):
		line=files[i].readline()
		if(line==""):
			files[i].close()
		parts=line.split(";",1)
		heaplist.append((parts[0],i,line))
	pq.heapify(heaplist)
while(count>0):
	elem=pq.heappop(heaplist)
	if(len(heaplist)>0 and elem[0]==heaplist[0][0]):
			temp=pq.heappop(heaplist)
			parts=elem[2].split(";",1)
			pq.heappush(heaplist,(temp[0],temp[1],temp[2].rstrip("\n")+parts[1]))
	else:	
		golbalfile.write(elem[2])
	if(files[elem[1]].closed is False):
		line=files[elem[1]].readline()
		if(line==""):
			count-=1
		else:
			parts=line.split(";",1)
			pq.heappush(heaplist,(parts[0],elem[1],line))


