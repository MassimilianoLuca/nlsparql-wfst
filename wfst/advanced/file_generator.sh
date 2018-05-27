#!/usr/bin/env bash
cd advanced
mkdir -p 'supporter'
for type in "train" "test"; do
	paste dataset/NLSPARQL.$type.feats.txt dataset/NLSPARQL.$type.data | cut -f 1,2,3,5 > supporter/$type.base
	cut -f 1,4 supporter/$type.base | sed 's/^\(.*\)\t\(O\)/\1\tO-\1/' | cut -f 2 > supporter/$type.concept_word.txt
	cut -f 2,4 supporter/$type.base | sed 's/^\(.*\)\t\(O\)/\1\tO-\1/' | cut -f 2 > supporter/$type.concept_pos.txt
	cut -f 3,4 supporter/$type.base | sed 's/^\(.*\)\t\(O\)/\1\tO-\1/' | cut -f 2 > supporter/$type.concept_lemma.txt
	paste supporter/$type.base supporter/$type.concept_word.txt supporter/$type.concept_pos.txt supporter/$type.concept_lemma.txt > supporter/$type.txt
done
cd supporter
rm train.base
rm train.concept_pos.txt
rm train.concept_lemma.txt
rm train.concept_word.txt
rm test.base
rm test.concept_pos.txt
rm test.concept_lemma.txt
rm test.concept_word.txt
cd ..
