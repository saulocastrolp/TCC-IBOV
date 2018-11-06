# -*- coding : utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

test = pd.read_csv('Historico_IBOVESPA.csv', delimiter=";", index_col=0, parse_dates=True, dayfirst=True ,dtype={'historico': int, 'fechamento' : int, 'varianca_dia': np.float64, 'abertura': np.float64, 'minimo': int, 'medio': int, 'maximo': int, 'volume': np.float64, 'negocios': int})

px = pd.DataFrame(test)

df = px.cumsum()
#graph = df.rolling(window=60).sum().plot(subplots=True)
df.plot(y="fechamento");

plt.show()
print(px)

