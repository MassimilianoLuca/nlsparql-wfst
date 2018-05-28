import operator
import csv

'''
Input:  [ ../wfst/base/dataset/NLSPARQL.train.data | ../wfst/base/dataset/NLSPARQL.test.data ] : str
'''

def word_counter(sourcefile="../wfst/base/dataset/NLSPARQL.train.data"):
    f = open(sourcefile,'r')

    word_instance = {}
    iob_tag_instance = {}
    for line in f:
        splitted = line.split()
        if(len(splitted)==2):
            if not splitted[0] in word_instance:
                word_instance[splitted[0]] = 1
            else:
                word_instance[splitted[0]] += 1
            if not splitted[1] in iob_tag_instance:
                iob_tag_instance[splitted[1]] = 1
            else:
                iob_tag_instance[splitted[1]] += 1

    # Sort to print a meaningful graph with word freqeuncy. Should be usefull to test Zipf's law
    sorted_word_instance = sorted(word_instance.items(), key=operator.itemgetter(1))
    sorted_word_instance.reverse()
    # Sort to print a meaningful graph with IOB tag
    sorted_tag_instance = sorted(iob_tag_instance.items(), key=operator.itemgetter(1))
    sorted_tag_instance.reverse()
    # Count the number of words and unique words (only usefull for the report)
    number_unique_word = len(word_instance)
    number_word = sum(word_instance.values())
    # Count the number of words and unique IOB tags (only usefull for the report)
    number_unique_tag = len(iob_tag_instance)
    number_tag = sum(iob_tag_instance.values())
    # Info for the report
    #print("#Unique words - TRAIN - %s" % number_unique_word)
    #print("#Words - TRAIN - %s" % number_word)
    #print("#Unique tags - TRAIN - %s" % number_unique_tag)
    #Should match with #Words... Check it to be a little bit more sure that the code is working properly
    #print("#Tags - TRAIN - %s" % number_tag)

    words_list, freqeuncy_list = zip(*sorted_word_instance)
    indexes = range(len(words_list))
    # write everything on a csv in order to plot the hist in a faster way
    with open('results.csv', 'w') as csv_results:
        writer = csv.writer(csv_results, delimiter=',')
        for i in range(len(words_list)):
            writer.writerow([words_list[i],freqeuncy_list[i]])

word_counter()
