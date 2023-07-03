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


num=[1/9, 0, 1]
den= np.polymul([1, 1], [1, 1, 1])

tf = sig.TransferFunction(num, den)

num_hp, den_hp = sig.lp2hp(num, den)
analyze_sys( sig.TransferFunction(num_hp, den_hp), 'HPF Objetivo' )

tf2 = sig.TransferFunction([1,0,0,0], den_hp)
analyze_sys( tf2, 'HPF Butter' )





