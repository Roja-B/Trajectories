#!/bin/bash -e
python prepare4R_NumComsAndModularities.py
#rm Work/RandIndecesOverTime_withUnsharedNodes.txt
python com_contingencytable_Rand.py
mkdir Results/ComContingencyTable1005
mkdir Results/TransitionProbs
mv Results/ComContingencyTable* Results/ComContingencyTable1005/
mv Results/TrProbs* Results/TransitionProbs/
#cp createplots.R Work
#cd Work
#R --save < createplots.R
#cd ..

# This is for creating the paths
python communityEvolution.py
i=1
Num=40
while [ $i -lt $Num ]; do
        python communityEvolutionPaths.py $i
#       python CommunityTopicBalatarin.py $i 
        i=$((i + 5))
        echo $i
done
## python communityEvolutionPathsTopics.py to get a list of topics for each community on the path of community evolutions


