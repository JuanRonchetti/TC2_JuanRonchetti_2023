# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:54:18 2023

@author: jron0
"""

import sympy as sp
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
from pytc2.sistemas_lineales import analyze_sys

plt.close('all')

# Se arma el pasabajos 
num= [1]
den= np.polymul([1, 1], [1, 1, 1])
tf_lp = sig.TransferFunction(num, den)

# Se plotea el pasabajos
analyze_sys( tf_lp, 'Pasa-bajos' )

# Se arma el pasaaltos y se plotea
num_hp, den_hp = sig.lp2hp(num, den)
analyze_sys( sig.TransferFunction(num_hp, den_hp), 'Pasa-altos' )
