import sympy
import numpy as np 

x = sympy.Symbol("x")
f = (x**2 - 1) / (x - 1)

r =sympy.limit(f, x, 1)

print(r)