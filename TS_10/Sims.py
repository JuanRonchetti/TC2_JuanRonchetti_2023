# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:42:36 2023

@author: jron0
"""

import sympy as sp
import numpy as np

from pytc2.sintesis_dipolo import foster, cauer_LC
from pytc2.dibujar import dibujar_foster_serie, dibujar_foster_derivacion, dibujar_cauer_LC
from pytc2.general import print_latex, print_subtitle, a_equal_b_latex_s

# Resolución simbólica
s = sp.symbols('s ', complex=True)

# --------------- Función de excitación ---------------
FF = ( (s**2 + 3)*(s**2 + 1) )/( (s**2 + 2) * s )
FF_y = 1/FF

print_latex(a_equal_b_latex_s('Z(s)', FF))
print_latex(a_equal_b_latex_s('Y(s)', FF_y))

k0, koo, ki_wi, _, FF_foster = foster(FF)

print_latex(a_equal_b_latex_s('k_0', k0))

print_latex(a_equal_b_latex_s(r'k_1 = \left[ \frac{1}{ \frac{1}{s. \frac{\omega_i^2}{2.k_i} } + s . \frac{1}{2.k_i} } \right]  = \
                                             \left[ \frac{1}{ \frac{k_0}{s} + s . k_\infty } \right] = \
                                             \left[ k_0, k_\infty \right] = \
                                       \left[ \
                                             \left[ \frac{\omega_1^2}{2k_1}, \frac{1}{2k_1} \right] \
                                       \right]', ki_wi ))

print_latex(a_equal_b_latex_s('k_\infty', koo))


print_latex(a_equal_b_latex_s(a_equal_b_latex_s('F(s)', FF)[1:-1], FF_foster ))
# --------------- Foster Derivación ---------------
print_subtitle('Foster Derivación')
k0, koo, ki_wi = foster(FF_y)
dibujar_foster_derivacion(k0, koo, ki_wi, y_exc = FF_y)

# --------------- Foster Serie ---------------
print_subtitle('Foster Serie')
k0, koo, ki_wi = foster(FF)
dibujar_foster_serie(k0, koo, ki_wi, z_exc = FF)