
./script_both1.sh 

after saving bipartite and unitpartite graphs:

00) move U-pol_J100VT5_stats.txt to /Work directory
0) save previous results in their own directory with a specific name and empty the Results directory
1) run ./step1.sh to run community finding on all the unipartite graphs
the file NumComsAndModularities will have directory name, number of coms, and modularity
2) copy NumComsAndModularities to ./Work/

note: run python usersPerWindow.py to create a file including all users in a time window

3)run ./getRelevant.sh (for Chi squared measure)
or ./getRelevant_h.sh (for binomial measure suggested by hazhir)

4) run ./rand.sh

---- skip these below:
4) run python prepare4R_NumComsAndModularities.py 
5) run python com_contingencytable_rand.py to get the rand index az well as transition probabilities 
6) run R and huse history to create plots of graph size, graph edges, graph denisity, Modularity, and number of coms, and rand indeces (or run source("createplots.R")
-----

5) run ./paths.sh 

---- skip these below:
7) run python communityEvolution.py to get the list of next communities from t1 to t2 over the whole timeline
8) run python communityEvolutionPaths.py to get the paths of community evolution over time. Here we need to specify a start time for when to begin looking at community evolution. this start time is hardcoded and it is in "number of windows"
9) run python CommunityTopicBalatarin.py  to get the topics most associated with Relevant Links in each community over the whole timeline
10) run python communityEvolutionPathsTopics.py to get a list of topics for each community on the path of community evolutions
-------------------

note: if number of nodes is less than 3 we should move on (com-finding will fail)
this issue also exists for any communities with less than 3 nodes
results are going to be in directory Results

6)run ./topUserRandplusPaths.sh

---- skip these below:
11) change path to correct directory and run python getTopUsers.py 
12) change path and run python comTopusers_contingencytable_Rand.py 
note that if we run this, things just keep getting appended to the rand index file, so we need to remove that each time.
move all TrProbs and TopUsersComCont... to the directories inside Results
13) change path and run communityEvolution.py
14) change path and run communityEvolutionPaths.py
-------------------

7) python createComEvolutionNetwork.py 
8) python CommunitySizesPath.py  
9) move CommunitySizes to the Visualize directory
10)run ./computeComQuality.sh > comQuality.txt

make random graph
shuf votes-summary.txt | head -3000 > randomVotes.txt
11) python findRandomDomains.py 
skip: 12) ./randomDomains.sh 
13) (change code to do this for radoms instead) 
python comQualityMeasure2.py > results.txt

for old datasets run this: (after changing the path to the correct directory)
python fixNumComModularities.py
move resulting file NumComModularities to the correct directory and ./Work
