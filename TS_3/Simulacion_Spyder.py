#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Juan Ronchetti
"""

from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

plt.close('all')

w02 = 1.965

my_tf = TransferFunction( [w02], [1, 2.509, 3.14, w02] )

bodePlot(my_tf, fig_id=1 )

pzmap(my_tf, fig_id=2) 




