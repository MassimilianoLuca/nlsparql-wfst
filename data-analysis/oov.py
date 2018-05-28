training = open('../wfst/base/dataset/NLSPARQL.train.data')
test = open('../wfst/base/dataset/NLSPARQL.test.data')

trainingSet = set()
testSet = set()
oovSet = set()

for line in training:
    tokens = line.split()
    if(len(tokens) >= 2):
        if tokens[0] not in trainingSet:
            trainingSet.add(tokens[0])

for line in test:
    tokens = line.split()
    if(len(tokens) >= 2):
        if(tokens[0]) not in testSet:
            testSet.add(tokens[0])

oovSet = testSet - trainingSet

print("OOV percentage: " +  str(len(oovSet)/float(len(testSet))))
