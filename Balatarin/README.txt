
1) extract politics links: 
python get_politics_links.py

2)


after saving bipartite and unitpartite graphs:

0) move U-pol_J100VT5_stats_combined.txt to /Work directory
1) run ./step1.sh to run community finding on all the unipartite graphs
the file NumComsAndModularities will have directory name, number of coms, and modularity
2) copy NumComsAndModularities to /Work
3) run python prepare4R_NumComsAndModularities.py 
4) run python com_contingencytable_rand.py 
5) copy RandIndecesOverTime.txt to /Work
5) run R and huse history to create plots of graph size, graph edges, graph denisity, Modularity, and number of coms, and rand indeces

note: if number of nodes is less than 3 we should move on (com-finding will fail)
this issue also exists for any communities with less than 3 nodes
results are going to be in directory ResultsJaccard30day14slide
