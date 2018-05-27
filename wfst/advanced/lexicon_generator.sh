#!/usr/bin/env bash
cd advanced
mkdir -p 'lexicon'
cut -f $1 supporter/train.txt | ngramsymbols - > lexicon/feature.lex
cut -f $2 supporter/train.txt | ngramsymbols - > lexicon/concept.lex
cut -f 4 supporter/train.txt | ngramsymbols - > lexicon/concept_iob.lex
