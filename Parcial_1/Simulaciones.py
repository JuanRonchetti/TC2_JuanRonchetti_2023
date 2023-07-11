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
from pytc2.general import print_subtitle

plt.close('all')

# Pasabajos
num= [0.714]
den= [1, 1.25, 1.53, 0.714]
tf_lp = sig.TransferFunction(num, den)
analyze_sys( tf_lp, 'LPF prototipo' )

# Pasaaltos
num_hp= [1, 0, 0, 0]
den_hp= [1, 2.14, 1.75, 1.4]
tf_hp = sig.TransferFunction(num_hp, den_hp)
analyze_sys( tf_hp, 'HPF objetivo' )





