from os import listdir
from os.path import isfile, join

mypath="title/"

onlyfiles = [int(f) for f in listdir(mypath) if isfile(join(mypath, f))]

print(sorted(onlyfiles))

secondryIndex=open("secondryTitleIndex","w+")

for i in sorted(onlyfiles):
	xyz=open(mypath+str(i),'r')
	line=xyz.readline()
	line=line.split(';',1)
	secondryIndex.write(line[0]+';'+str(i)+'\n')