# Basic Stages (inorder) 
# Tokenization: remove punctuation, dont remove hyphens
# case folding: usally lower
# stop words: remove them serach engine dont use stop words
# stemming and lemmatiztioin: stemming is fast, lemmatiztioin is smart
# posting List  
# optimization

# kinds of preProcessing or data Extracted

# 1. Ttitle -> processTitle
# 2. body text -> processText
# 3. infobox -> processText
# 4. externalLinks links -> externalLinks
# 5. categories -> processText
# 6. references -> processText

# TO-DO dynamic stemming
# (Done) TO-DO return body[0] externalLinks and
# if part update: categories in last no body[0]
# TO-DO optimize pre process text

from collections import defaultdict

def load_stopwords():
	stopwords=defaultdict(bool)
	with open("stop_words.txt",'r') as file:
		for word in file:
			word=word.strip(' ').strip('\n');
			stopwords[word]=True;
	# some of wiki specific stopwords 
	stopwords['category']=True;
	stopwords['Template']=True;
	stopwords['ref']=True;
	stopwords['br']=True;
	return stopwords;


class preProcessor():
	def __init__(self):
		self.stopwords=load_stopwords();
	
	def tokenise(self,data,regex=r'[a-z]+'):
		import re
		data=data.lower()
		tokens=[]
		tokens=re.findall(regex,data);
		return tokens

	def removeStopWords(self,tokenList):
		tokens=[]
		tokens=[word for word in tokenList if self.stopwords[word]==False]
		return tokens

	def stemming(self,tokenList):
		import nltk
		stemmer = nltk.stem.SnowballStemmer('english');
		tokens=[]
		# TO-DO I have to add dynamic stemming  
		for token in tokenList:
			word=stemmer.stem(token);
			tokens.append(word)
		return tokens

	def tokenisStopWordsStemming(self,data,regex=r'[a-z]+'):
		tokens=self.tokenise(data,regex);
		tokens=self.removeStopWords(tokens);
		tokens=self.stemming(tokens);
		return tokens

	def processTitle(self,data):
		regex=r'\d+|[\w]+'
		tokens=self.tokenisStopWordsStemming(data,regex)
		# print(tokens);

	def externalLinks(self,data):
		# * [https://digitalalabama.com Your Not So Ordinary Alabama Tourist Guide] *
		body=data.split("==external links==");
		links=[]
		#if links are not present
		if(len(body)<2): return links
		lines=body[1].split('\n')
		for line in lines:
			if('*[' in line or '* ['):
				words=line.split(' ')
				# print(words)
				for word in words:
					# dont include www 
					if('http' not in word):
						links.append(word)
		#TO-DO check for encoding 
		link_body=' '.join(links)
		tokens=self.tokenisStopWordsStemming(link_body)
		# print(tokens)
		return tokens

	def processText(self,data):
		data=data.lower()
		# area_land_sq_mi
		# it is also standard practice to ...
		data = data.replace('_',' ');
		data = data.replace('-',' ');
		# County,
		data=data.replace(',','')
		# Alabama|Greate
		data=data.replace('|',' ')

		# dont change data from here it is used later
		
		lines=data.split('\n')
		n=len(lines)
		infobox=[]
		catgories=[]
		references=[]
		body=[]
		infoboxParethesis=0
		referencesParenthesis=0
		elinks=True;

		# if not infobox and categorories and cite(<ref></ref>) apppend to body
		# else append to infbox catgories cite respectively
		i=0
		while(i<n):
			if('{{infobox' in lines[i]):
				line=lines[i].split('{{infobox')
				body.append(line[0])
				infobox.append(line[1])
				# i can optimize here
				infoboxParethesis+=1
				infoboxParethesis+=line[1].count('{{')-line[1].count('}}')
				i+=1
				while infoboxParethesis>0 and i<n:
					infoboxParethesis+=lines[i].count('{{')-lines[i].count('}}')
					infobox.append(lines[i])
					i+=1
			elif('{{cite' in lines[i]):
				line=lines[i].split('{{cite')
				references.append(line[1])
				# i can optimize here
				referencesParenthesis+=1
				referencesParenthesis+=line[1].count('{{')-line[1].count('}}')
				i+=1
				while referencesParenthesis>0 and i<n:
					referencesParenthesis+=lines[i].count('{{')-lines[i].count('}}')
					references.append(lines[i])
					i+=1
			elif(elinks):
				if('[[category' in lines[i] or '==external links==' in lines[i]):
					elinks=False
				else:
					body.append(lines[i])
					i+=1
			elif('[[category' in lines[i]):
				# [[Category:Libertarianism]] [[Category:Political culture]]
				line=lines[i].replace('[[Category:','').replace(']]','')
				catgories.append(line)
				i+=1
			else:
				i+=1
		infoboxString=' '.join(infobox)
		infoboxTokens=self.tokenisStopWordsStemming(infoboxString)

		externalLinksTokens=self.externalLinks(data)
		print(infoboxTokens)
