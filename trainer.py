import pandas as pd
from normalize import *

fileName = './training-data/cs_170_small80.txt'     # Change from 80 -> 8

def main():
    data = pd.read_csv(fileName, header=None, delim_whitespace=True)
    print('Raw Data:\n', data, '\n', sep='')
    normalize(data)
    print('Normalized Data:\n', data, sep='')

if __name__ == '__main__':
    main()
