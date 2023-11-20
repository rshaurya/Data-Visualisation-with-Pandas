import pandas as pd

# function to create dataframe of index

def index_dataframe(rows):
    d = {}
    df = pd.read_csv('crypto-dataset/Index/Index.csv', index_col=0, nrows=rows)
    for i in df['Symbol']:
        d[i] = "#0ee0e8"
    return d

print(index_dataframe(10))

