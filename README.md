					## WIKIPEDIA SEARCH ENGINE ##

The mini project involves building a search engine on the Wikipedia Data Dump without using any external index. For this project, I use the data dump of size ~54 GB. The search results return in real time. Multi-word and multi-field search on Wikipedia Corpus is implemented.

You also need to rank the documents and display only the top 10 most relevant documents.

#### Key challenge

To implement multi level data indexing to provide on demand search results(i.e in less than a sec) in memory through disk reads.

#### How things are done:

Etree is used to parse the XML Corpus without loading the entire corpus in memory. This helps parse the corpus with minimum memory. After parsing the following morphological operations are performed to obtain clean vocabulary.

`Tokenisation`	   : Tokenisation is done using regular expressions.

`Casefolding` 	   : Casefolding is easily done through lower().

`Stemming`    	   : It is done using snowfall stemmer part of nltk library of python.

`Stop Word Removal`: Stop words are removed by referring a stop word list that is maintained in a seperate file.
include terms like redirect,URL,png, HTTP etc.

`Term filter`      : This removes some of the common terms that are found in abundance in all the pages. These 
