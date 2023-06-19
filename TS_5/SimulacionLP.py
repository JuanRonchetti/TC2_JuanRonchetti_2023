# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:54:18 2023

@author: jron0
"""

import sympy as sp
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
from pytc2.sistemas_lineales import analyze_sys, tf2sos_analog, pretty_print_SOS, pretty_print_lti

plt.close('all')

# Se arma el pasabajos 
num= [0.714]
den= [1, 1.25, 1.53, 0.714]
tf_lp = sig.TransferFunction(num, den)

# Se plotea el pasabajos
#analyze_sys( tf_lp, 'LPF prototipo' )

num_bp= [5.7e-3, 0, 0, 0]
den_bp= [1, 0.25, 3.06, 0.5057, 3.06, 0.25, 1]
tf_bp = sig.TransferFunction(num_bp, den_bp)
#analyze_sys( tf_bp, 'BPF objetivo' )

bp_SOS = tf2sos_analog(num_bp, den_bp)

analyze_sys( bp_SOS )

pretty_print_SOS(bp_SOS)

pretty_print_SOS(bp_SOS, mode='omegayq')



