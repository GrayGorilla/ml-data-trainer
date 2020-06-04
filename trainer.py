import pandas as pd
from normalize import *
from validator import leaveOneOutVal as validator
from search import forwardSelection as searchFeatures

defaultFile = './training-data/cs_170_small80.txt'     # Change from 80 -> 8

def getData():
    print('\n-------- Welcome to Nathan D. Brennan\'s Feature Selection Algorithm. --------')
    fileName = input('Press enter to use the default file, or type in the name of the file to test: ')
    if fileName:
        data = pd.read_csv(fileName, header=None, delim_whitespace=True)
    else:
        data = pd.read_csv(defaultFile, header=None, delim_whitespace=True)
    print(f'\nThis dataset has {len(data.columns) - 1} features (not including the class attribute), with {len(data)} instances.\n')
    return data

def trainModel(data):
    # Normalize data
    print('Please wait while I normalize the data...', end=' ')
    normalize(data)
    print('Done!\n')
    # Introduce Algorithms
    features = list(data.columns[1:])
    accuracy = validator(data, features)
    print(f'Running "Forward Selection" & "Nearest Neighbor" with all {len(features)} features, using "Leaving-One-Out" evaluation, I get an accuracy of', '{:.1%}\n'.format(accuracy))
    # Find best features
    searchFeatures(data)

def main():
    data = getData()
    trainModel(data)

if __name__ == '__main__':
    main()
