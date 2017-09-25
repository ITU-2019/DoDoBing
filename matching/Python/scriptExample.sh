#!/bin/sh
for FILE in ../data/*-in.txt

do
	echo $FILE
	base=${FILE%-in.txt}
    python main.py $FILE > ../data/$base.group-o.out.txt # replace with your command!
    diff -q ../data/$base.group-o.out.txt ../data/$base-out.txt
done
