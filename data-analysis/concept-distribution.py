import operator
import matplotlib.pyplot as plt

'''
Input:  [ ../wfst/base/dataset/NLSPARQL.train.data | ../wfst/base/dataset/NLSPARQL.test.data ] : str
'''

def word_counter(sourcefile="../wfst/base/dataset/NLSPARQL.train.data"):
    f = open(sourcefile,'r')

    concept_instance = {}
    for line in f:
        splitted = line.split()
        #Take the tag and normalize it: delete O, I-, B-
        if(len(splitted)==2):
            normalized_concept = splitted[1].replace("I-","").replace("B-","")
            if splitted[1]=='O':
                continue
            if not normalized_concept in concept_instance:
                concept_instance[normalized_concept] = 1
            else:
                concept_instance[normalized_concept] += 1

    # Sort to print a meaningful graph with concepts
    sorted_concept_instance = sorted(concept_instance.items(), key=operator.itemgetter(1))
    sorted_concept_instance.reverse()

    # movie.name is the most common concept. Print to probability to write something in the report
    print(concept_instance["movie.name"]/sum(concept_instance.values()))

    concept_list, freqeuncy_list = zip(*sorted_concept_instance)

    indexes = range(len(concept_list))

    plt.bar(indexes, freqeuncy_list)
    plt.xticks(indexes, concept_list)
    plt.show()

word_counter()
