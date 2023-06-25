from sympy import *
# from scipy.misc import derivative
import numpy as np
from findiff import FinDiff


def f(x):
    # ppar = [4, 3, -2, 10]
    # return np.poly1d(ppar)
    return (7*(x**3)) + (x**2) + 1

# # print(derivative(f, x).doit())

# - Using sympy
x = Symbol('x')

print(diff(x**5))


# - Using FinDiff
x = np.linspace(0, 10, 100)
dx = x[1] - x[0]
f = np.sin(x)
g = np.cos(x)

d2_dx2 = FinDiff(0, dx, 2)

result_f = d2_dx2(f)
result_g = d2_dx2(g)


'''
The arrays result_fand result_g have the same shape as 
the arrays f and g and contain the values of the second derivatives
'''

