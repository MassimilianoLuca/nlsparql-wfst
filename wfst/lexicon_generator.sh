#!/usr/bin/env bash
mkdir -p 'lexicon'
cut -f $1 supporter/train.txt | ngramsymbols - > lexicon/feature.lex
cut -f 4 supporter/train.txt | ngramsymbols - > lexicon/concept.lex
