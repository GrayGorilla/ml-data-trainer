from validator import leaveOneOutVal as validator

def forwardSelection(dataFrame):
    chosenFeatures = []
    globalMax = 0
    featureSize = 0
    cols = list(dataFrame.columns)
    cols.remove(0)
    print('\nBegining Search.\n')
    # Traverse through each level of Feature Tree
    for level in range(1, len(cols) + 1):
        print(f'\tLevel of Feature Tree: {level}')
        localMax = 0
        bestFeature = None
        # Find most accurate feature combination of this level
        for feature in cols:
            # Don't compare if feature already chosen
            if feature in chosenFeatures:
                continue
            # Compare accuracy with local maxima
            chosenFeatures.append(feature)
            accuracy = validator(dataFrame, chosenFeatures)
            print(f'\tUsing feature(s) {chosenFeatures} accuracy is', '{:.1%}'.format(accuracy))
            if accuracy > localMax:
                localMax = accuracy
                bestFeature = feature
            chosenFeatures.pop()
        chosenFeatures.append(bestFeature)
        print()
        # Update global maxima
        if localMax > globalMax:
            globalMax = localMax
            featureSize = level
        elif localMax < globalMax:
            print('(Warning: Accuracy has decreased! Continuing search in case of local maxima)')
        else:
            print('(Warning: No change in accuracy. Continuing search in case of local maxmia)')
        print(f'Feature set {chosenFeatures} was best, accuracy is', '{:.1%}\n'.format(localMax))
    # Print results
    chosenFeatures = chosenFeatures[0:featureSize]
    print('----------------------\n')
    print(f'Finished search! The best feature subset is {chosenFeatures} which has an accuracy of,', '{:.1%}\n'.format(globalMax))
