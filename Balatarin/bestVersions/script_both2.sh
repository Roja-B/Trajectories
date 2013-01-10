#"! 

index=0
window=30
end=1534
mkdir /media/data3/allen/unipartite/W30S30
while [ $index -le $end ]
  python makeUnipartiteGraph_pro.py $index $window W30S30
  index=$(( $index + 30 ))
  echo $index
done


index=0
window=30
end=1534
while [ $index -le $end ]
  python extract_bipartite_pro.py $index $window
  index=$(( $index + 30 ))
  echo $index
done

mkdir /media/data3/allen/bipartite/W30S30
mv /media/data3/allen/bipartite/*.txt /media/data3/allen/bipartite/W30S30


index=0
window=14
end=1534
while [ $index -le $end ]
  python extract_bipartite_pro.py $index $window
  index=$(( $index + 14 ))
  echo $index
done
mkdir /media/data3/allen/bipartite/W14S14
mv /media/data3/allen/bipartite/*.txt /media/data3/allen/bipartite/W14S14
