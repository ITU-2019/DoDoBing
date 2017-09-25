#!/bin/bash
[ -e out.txt ] && rm out.txt
for f in ../data/*-tsp.txt
do
  echo $f
  base=${f%-tsp.txt}
  # echo $base
  t=$(python main.py $f)
  o=${t%---*}
  echo "${base}.tsp: ${o}" >> closest-pair-out-group0.txt
done
