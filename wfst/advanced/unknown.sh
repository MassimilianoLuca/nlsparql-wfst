#!/usr/bin/env bash
cd advanced
# consider <unk> for unk words
# credits: Evegeny Stepanov, Ph.D.
n=$(wc -l counter/concept_counter.txt | sed 's/^ *\([0-9]\+\).*$/\1/')
prob=$(echo "-l(1/$n)" | bc -l)
while read concept ___
do
   echo "0\t0\t<unk>\t$concept\t$prob"
done < counter/concept_counter.txt >> counter/feature_to_concept_transducer.txt
# end state
echo "0" >> counter/feature_to_concept_transducer.txt
