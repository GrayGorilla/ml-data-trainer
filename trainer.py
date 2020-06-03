import pandas as pd
from normalize import normalize

fileName = './training-data/cs_170_small8.txt'

def main():
    rawData = pd.read_csv(fileName, header=None, delim_whitespace=True)
    print('Raw Data:')
    print(rawData)
    print()
    normalizedData = normalize(rawData)
    print('Normalized Data:')
    print(normalizedData)

if __name__ == '__main__':
    main()
