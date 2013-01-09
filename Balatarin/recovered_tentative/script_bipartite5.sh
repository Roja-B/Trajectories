#"! 
index=0
window=30
end=0
while [ $index -le $end ]
  python extract_bipartite_pro.py $index $window
  index=$(( $index + 14 ))
  echo graph created
done
