Creation of index is done in three parts

First you create 34 inverted idices (from 34 wiki dump) using main.py then  (2nd) merge using merge.py (k-way merge) (3rd)split using split.py  and it also creates secondry index
doc title is also splited after evrey 1 lakh lines 

Query format:
k results;query
query can be multifield and or simple

Query Output:
Unique page id, unique page title