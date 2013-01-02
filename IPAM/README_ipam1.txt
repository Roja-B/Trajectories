PREPARATION:

00) create list of email addresses to be resolved
0) run source("bipartiteAnalysis.R") this produces degree distributions of programs and participants

-------
CREATE GRAPHS:

1) run python userProgramEdgelist.py 
(this program creates edgelists, it also automatically omits programs in the file OMITlist)
2) run python resolveEmails.py to resolve emails
3) run python divideTemporally.py to create temporally divided edgelists
4) run python makeBipartite.py to create bipartite graphs with desired window size and sliding amount
5)run python projectGraph_programs.py to create unipartite graphs

-------
CREATE COMMUNITIES:

6) run ./step1.sh to execute  main_ipam.R and create communities per time

-------
CREATE PATHS:
7) find transition probabilities
run python transitionProbs_ipam.py (TODO)
 
7) run ./paths.sh
