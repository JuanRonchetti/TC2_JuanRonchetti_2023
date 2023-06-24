# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 13:33:41 2023

@author: jron0
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.close('all')

modulo  = pd.read_csv("Pre TPLAB.csv")

modulo.plot(kind='line', x='X (Hz)',y='Vo/Vi (dB)', logx=True, grid=True)


