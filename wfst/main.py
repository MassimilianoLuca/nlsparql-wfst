import sys
import os
import math

# folder path
DATASET_FOLDER = "dataset/"
COUNTER_FOLDER = "counter/"
LEXICON_FOLDER = "lexicon/"
SUPPORTER_FOLDER = "supporter/"

#read parameters and check for validity:
#1) ['word' | 'pos' | 'lemma']
#2) n-gram order
#3) ['witten_bell' | 'absolute' | 'katz' | 'kneser_ney' | 'presmoothed' | 'unsmoothed']

if( len(sys.argv) != 4 ):
    print("Wrong usage. Please specify: \n - feature: ['word' | 'pos' | 'lemma'] \n - order: n-gram order (integer number) \n - method: ['witten_bell' | 'absolute' | 'katz' | 'kneser_ney' | 'presmoothed' | 'unsmoothed']")
    raise SystemExit
feature = ""
order = sys.argv[2]
method = ""
if( sys.argv[1] in ['word','pos','lemma'] ):
    if(sys.argv[1] == 'word'):
        feature = 1
    elif(sys.argv[1] == 'pos'):
        feature = 2
    else:
        feature = 3
else:
    print("The specified 'method' is not valid")
    raise SystemExit
if( sys.argv[3] in ['witten_bell','absolute','katz','kneser_ney','presmoothed','unsmoothed'] ):
    method = sys.argv[3]
else:
    print("The specified 'method' is not valid")
    raise SystemExit
# generate files
os.system('sh ./file_generator.sh')
# generate lexicons using ngramsymbols.
# the result of this procedure depends on the feature selected
os.system('sh ./lexicon_generator.sh ' + str(feature))
# count features, concepts and <feature, concept>
os.system('sh ./counter.sh ' + str(feature))
# compute <feature, concept> probability
features = []
concepts = []
concepts_value = []
feature_concept_counter = []
concpet_counters = {}
feature_concept_probability = []
# read the file containing feature, concepts and <feature, concept> counter
with open(COUNTER_FOLDER + 'feature_concept_counter.txt', 'r', encoding='utf-8') as feature_concept_file:
    for line in feature_concept_file:
        tokenized = line.split()
        if(len(tokenized) == 3):
            # add a feature
            features.append(tokenized[0])
            # add a concept
            concepts.append(tokenized[1])
            # add the counter
            feature_concept_counter.append(int(tokenized[2]))
    feature_concept_file.close()
# read the file containing the number of instances for each concept
with open(COUNTER_FOLDER + 'concept_counter.txt', 'r', encoding='utf-8') as concept_file:
    for line in concept_file:
        tokenized = line.split()
        if(len(tokenized) == 2):
            concpet_counters[tokenized[0]] = int(tokenized[1])
    concept_file.close()
# substitute the concept with the number of instances of that concept
for i in range(len(concepts)):
    concepts_value.append(concpet_counters[concepts[i]])

for i in range(len(concepts)):
    feature_concept_probability.append(- math.log(feature_concept_counter[i] / concepts_value[i]))

with open(COUNTER_FOLDER + 'feature_concepts_probability.txt', 'w', encoding='utf-8') as feature_concept_probability_file:
    for element in feature_concept_probability:
        feature_concept_probability_file.write(str(element) + '\n')
    feature_concept_probability_file.close()
# create the transducer file
with open(COUNTER_FOLDER + 'feature_to_concept_transducer.txt', 'w', encoding='utf-8') as f2c:
    for i in range(len(features)):
        f2c.write('0 0 '+ features[i] + ' ' + concepts[i] + ' ' + str(feature_concept_probability[i]) + '\n')
    f2c.close()
# compute the <unk> and add the result to feature_to_concept_transducer.txt
os.system('sh ./unknown.sh')
# openfst commands. For further information check logic.sh
os.system('sh ./logic.sh '+ str(feature) +' '+ str(order)+' '+ method)
# evaluate the results
# openfst commands. For further information check logic.sh
os.system('sh ./results.sh '+ str(sys.argv[1]) +' '+ str(order)+' '+ method)
