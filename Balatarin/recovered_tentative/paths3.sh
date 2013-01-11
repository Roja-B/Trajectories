PATH="."
python getTopUsers.py $PATH
python comTopusers_contingencytable_Rand.py $PATH
#note that if we run this, things just keep getting appended to the rand index file, so we need to remove that each time.
mv Results/TrProbs* Results/TransitionProbs
mv Results/TopUser* Results/ComContingencyTable1005
python communityEvolution.py
python  communityEvolutionPaths.py
#"! 
