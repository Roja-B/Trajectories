#"! 
#/media/data3/allen/unipartite.sh
index=0
window=60
end=1534
mkdir /media/data3/allen/unipartite/W60S28
while [ $index -le $end ]
  python makeUnipartiteGraph_pro.py $index $window W60S28
  index=$(( $index + 28 ))
  echo $index
done
mkdir /media/data3/allen/unipartite/W30S7
index=0
window=30
end=1534
while [ $index -le $end ]
  python makeUnipartiteGraph_pro.py $index $window W30S7
  index=$(( $index + 7 ))
  echo $index
done

