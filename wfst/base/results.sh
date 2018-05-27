#!/usr/bin/env bash
cd base
# generate a file which is compatible with conlleval.pl
mkdir -p "results"
paste supporter/test.txt results/result.txt | cut -f 1,4,9 > supporter/comparison.txt
perl conlleval.pl -d '\t' < supporter/comparison.txt > results/$1_$2_$3.txt

rm -r counter
rm -r extractor
rm -r language_modeler
rm -r lexicon
rm -r model
rm -r supporter
