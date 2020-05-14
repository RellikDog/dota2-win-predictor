import pandas as pd 
import numpy as np 

def fix_cols(df):
    fdf = df.rename(columns={0: 'winner',
                   1: 'region',
                   2: 'mode',
                   3: 'type'})
    fdf.columns = [(i-3) if type(i) == int else i for i in fdf.columns]
    return fdf

def rf_fix_n_split(df):
    rfdf = df.copy()
    for i in ['region', 'mode', 'type']:
        rfdf.pop(i)
    winner = rfdf.pop('winner')
    y = winner.replace(-1, 0)
    #make X values binary, each column is char-team, 1 denotes picked.
    X = rfdf
    X2 = X.copy()
    X.columns = [(str(i) + 'A') for i in X.columns]
    X2.columns = [(str(i) + 'B') for i in X2.columns]
    X.replace(-1, 0, inplace=True)
    X2.replace(1, 0, inplace=True)
    X2.replace(-1, 1, inplace=True)
    X = pd.concat([X, X2], axis=1)
    return X, y