#!/usr/bin/env bash
cd base
mkdir -p 'counter'
cut -f $1 supporter/train.txt | cat - | sed '/^[ \t]*$/d' | sort | uniq -c | sed 's/^ *//' | awk '{OFS="\t"; print $2,$1}' > counter/feature_counter.txt
cut -f 4 supporter/train.txt | cat - | sed '/^[ \t]*$/d' | sort | uniq -c | sed 's/^ *//' | awk '{OFS="\t"; print $2,$1}' > counter/concept_counter.txt
cut -f $1,4 supporter/train.txt | cat - | sed '/^[ \t]*$/d' | sort | uniq -c | sed 's/^ *//' | awk '{OFS="\t"; print $2,$3,$1}' > counter/feature_concept_counter.txt
