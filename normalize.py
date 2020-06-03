def normalize(data):
    cols = list(data.columns)
    cols.remove(0)
    
    for col in cols:
        data[col] = (data[col] - data[col].mean()) / data[col].std()
