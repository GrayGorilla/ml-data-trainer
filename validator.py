from classifier import nearestNeighbor as classifier

def leaveOneOutVal(dataFrame, features):
    classes = dataFrame[0]
    selectData = dataFrame[features]
    score = 0
    # Test the classifier: One test data point vs everything else (training data)
    for testDataPt in range(0, len(selectData)):
        guess = classifier(selectData, classes, testDataPt)
        if guess == classes[testDataPt]:
            score += 1

    return score / len(selectData)
