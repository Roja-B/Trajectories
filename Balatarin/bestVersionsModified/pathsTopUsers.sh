#!/bin/bash
MYPATH="."
python getTopUsers.py $MYPATH
rm Work/RandIndecesOverTime_TopUsers.txt
python comTopusers_contingencytable_Rand.py $MYPATH
#note that if we run this, things just keep getting appended to the rand index file, so we need to remove that each time.
mv Results/TrProbs* Results/TransitionProbs
mv Results/TopUser* Results/ComContingencyTable1005
python communityEvolutionTopUsers.py $MYPATH
Num=20
while [ $i -lt $Num ]; do
        python communityEvolutionPathsTopUsers.py $MYPATH $i
        i=$((i + 5))
        echo $i
done


