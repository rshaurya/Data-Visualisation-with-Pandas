import pandas as pd
import matplotlib.pyplot as plt

# function to create dataframe based on index

def crypto_dataframe(symbol, name):
    df = pd.read_csv('crypto-dataset/Price-Data/' + symbol + '_' + name + '.csv', index_col=0)
    print(df)
    return df

# method to create plots

df = crypto_dataframe('ADA', 'Cardano')

df['Volume'].plot()
plt.show()
