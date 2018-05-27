#!/usr/bin/env bash

# Parameters:
# $1 = feature
# $2 = ngram_order
# $3 = ngram_method

cd base

# generate the fst file of counter/feature_to_concept_transducer.txt
fstcompile --isymbols=lexicon/feature.lex --osymbols=lexicon/concept.lex counter/feature_to_concept_transducer.txt | fstarcsort - > counter/feature_to_concept_transducer.fst
# create phrases from the train file (requested to run farcompilestrings)
# credits: Evgeny Stepanov
mkdir -p 'language_modeler'
cut -f 4 supporter/train.txt | cat - | sed 's/^ *$/#/g' | tr '\n' ' ' | sed 's/ # /\n/g' > language_modeler/train_concpet_to_phrases.txt
cut -f $1 supporter/test.txt | cat - | sed 's/^ *$/#/g' | tr '\n' ' ' | sed 's/ # /\n/g' > language_modeler/test_concpet_to_phrases.txt
# compile the file created the line above into .far
farcompilestrings --symbols=lexicon/concept.lex --unknown_symbol='<unk>' --keep_symbols=1 language_modeler/train_concpet_to_phrases.txt > language_modeler/concepts.far
# apply the correct model
ngramcount --order=$2 language_modeler/concepts.far > language_modeler/concepts.counts
ngrammake --method=$3 language_modeler/concepts.counts > language_modeler/concepts.lm
mkdir -p 'model'
fstcompose counter/feature_to_concept_transducer.fst language_modeler/concepts.lm > model/model.fst
farcompilestrings --symbols=lexicon/feature.lex --unknown_symbol='<unk>' language_modeler/test_concpet_to_phrases.txt > language_modeler/sentences.far
mkdir -p 'extractor'
cd extractor
farextract --filename_suffix='.fsa' ../language_modeler/sentences.far
cd ..
for filename in extractor/*.fsa; do
    fstcompose $filename model/model.fst | fstshortestpath | fstrmepsilon  | fsttopsort | \
		fstprint --isymbols=lexicon/feature.lex --osymbols=lexicon/concept.lex | \
		sed 's/^[0-9]*$//' | cut -f 3,4 > $filename.res
done
# compose all the .res file produced by the for statement
mkdir -p "results"
cat extractor/*.res > results/result.txt
