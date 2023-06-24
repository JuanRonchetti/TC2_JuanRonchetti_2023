# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 13:33:41 2023

@author: jron0
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.close('all')

modulo  = pd.read_csv("modulo2.csv")
fase  = pd.read_csv("fase2.csv")

fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True)

modulo.plot(kind='line', ax=axes[0], x='X (Hz)',y='Ch-1 (dBr)', logx=True, grid=True)

fase.plot(kind='line', ax=axes[1], x='X (Hz)',y='Ch-1 (deg)', logx=True, grid=True)

