

#!/bin/bash
x=1
y=30
while [ $x -le $y ]do  
	python makeUnipartite_pro.py 12/$x/2008 30  
	x=$(( $x + 14 ))
done



window = 30
end = 1534
while[ $index -le $end ]do  
python extract_bipartite_pro.py $index $window  
index=$(( $index + 14 ))
done
