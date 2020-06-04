import math

def nearestNeighbor(selectData, classes, testDataPt):
    closestPoint = None
    minDistance = math.inf
    data = selectData.values
    # Find closest training data point to test data point
    for trainDataPt in range(0, len(data)):
        # Don't test against itself
        if trainDataPt == testDataPt:
            continue
        # Get Euclidean Distance in N-Dimensional space
        x = data[testDataPt]
        y = data[trainDataPt]
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
        if distance < minDistance:
            minDistance = distance
            closestPoint = trainDataPt
    return classes[closestPoint]
