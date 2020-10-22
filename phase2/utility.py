import sys
import os

indexPath=""
statPath=""

def getCurrentPath():
	return os.getcwd()

def setCurrentPath():
	pass

def setIndexPath(data="inverted_index/"):
	global indexPath
	indexPath= getCurrentPath()+'/'+ data + 'index'

def  getIndexPath():
	global indexPath
	return indexPath

def setStatPath(data="stat"):
	global statPath
	statPath= getCurrentPath()+'/'+ data

def  getStatPath():
	global statPath
	return statPath

def progress(count, total, status=''):
	bar_len = 60
	filled_len = int(round(bar_len * count / float(total)))

	percents = round(100.0 * count / float(total), 1)
	bar = '#' * filled_len + '-' * (bar_len - filled_len)

	sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
	sys.stdout.flush()