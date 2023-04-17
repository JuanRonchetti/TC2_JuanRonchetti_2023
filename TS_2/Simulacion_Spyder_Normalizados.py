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

R1n = 0.1
R2n = 3
R3n = 1
Cn=1 

Q=R2n/R3n

my_tf = TransferFunction( [-(R3n/R1n)], [1, 1/Q, 1] )

bodePlot(my_tf, fig_id=1 )

pzmap(my_tf, fig_id=2) 




