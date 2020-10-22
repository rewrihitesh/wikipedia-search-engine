					## WIKIPEDIA SEARCH ENGINE ##

The mini project involves building a search engine on the Wikipedia Data Dump without using any external index. For this project, I use the data dump of size ~54 GB. The search results return in real time. Multi-word and multi-field search on Wikipedia Corpus is implemented.

I also wrote a page ranking algorithm to show you to show you top "k" document.

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

**NOTE** One major optimization is done in stemming to reduce time of indexing is that, till 50000 document any repeatative word is not again stemmed,i.e we have used dynamic programming based approach here because stemming is time consuming and this has reduced indexing time to half.

#### As a part of Primary Inverted Index we have 4 files

. `titlePosting`    :It contain docid and tf-idf of word part of document title with respect to a document.

. `CategoryPosting` :It contain docid and tf-idf of word part of category field with respect to a document.

. `InfoBoxPosting`  :It contain docid and tf-idf of corresponding word part of infobox fild with respect to a document.

. `textPosting`:    :It contain docid and tf-idf of corresponding word part of text,references and external links with respect to a document.

Secondary Index:

. `WordPosition`    :It keep the track of posting list of word in title,infobox,text and category and allow as **O(log(n))** access to them and 			   worked as a secondary index above field wise inverted index.

		  `XYX:{d:45454 t:45142 c:4587574 i:4545870}`

**Ranking Factor**
While building index ranking of top 10 document corresponding to a word is done using td-idf and build a champion list and write into file.

**Merging all temporary indexes using block based external merge sort algorithm**
I have wote eficent K-Way Merge sort to sort the presorted multiple indeices.

#### Term Field Abbreviations For Search:

. Infobox abbreviated as i

. Body abbreviated as b

. Title abbreviated as t

. External Link abbreviated as e

. References abbreviated as r 

. Category abbreviated as c


#### Query Format

. `Field Query`  : t:abc b:xyz c:xxy i:dde e:ref r:ext

. `Normal Query` : word1 wor2 word3

#### TO DO

. auto search wikipedia dump and automate index creation 
. make simplified web app
