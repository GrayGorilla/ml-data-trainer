import pandas as pd
from normalize import *
from search import forwardSelection as searchFeats

fileName = './training-data/cs_170_small80.txt'     # Change from 80 -> 8

def main():
    data = pd.read_csv(fileName, header=None, delim_whitespace=True)
    print('Raw Data:\n', data, '\n', sep='')
    print('Please wait while I normalize the data...', end=' ')
    normalize(data)
    print('Done!\n')
    print('Normalized Data:\n', data, sep='')
    searchFeats(data)

if __name__ == '__main__':
    main()
