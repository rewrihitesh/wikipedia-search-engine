# import heapq as pq

# noOfFiles=67

# fname=["title"+str(i) for i in range(0,noOfFiles)]

# print(fname)

# files=[open(str(i),"r") for i in fname]

# # intialize heap

# heaplist=[]

# # pq.heapify(heaplist)

# # print(heaplist[0])

# # print(pq.heappop(heaplist))
# count=noOfFiles
# golbalfile= open("sort.txt","w+")

# for i in fname:
# 	if(files[i].closed is False):
# 		line=files[i].readline()
# 		if(line==""):
# 			files[i].close()
# 		parts=line.split(";",1)
# 		heaplist.append((parts[0],i,line))
# 	pq.heapify(heaplist)
# while(count>0):
# 	elem=pq.heappop(heaplist)	
# 	golbalfile.write(elem[2])
# 	if(files[elem[1]].closed is False):
# 		line=files[elem[1]].readline()
# 		if(line==""):
# 			count-=1
# 		else:
# 			parts=line.split(";",1)
# 			pq.heappush(heaplist,(parts[0],elem[1],line))

titleDict={}

file = open("doctitle.txt","r")
for i in file:
 	split=i.split(';',1)
 	titleDict[int(split[0])]=split[1]

file1=open("sort","w+")

for key in sorted(titleDict):
	file1.write(str(key)+';'+titleDict[key])

