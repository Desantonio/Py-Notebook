
from sympy import symbols, sin, cos, tan, integrate, diff, plot
from sympy import *
import matplotlib.pyplot as plt

x = symbols("x")
function = sin(x)**cos(x)/tan(2*x)
integrate_function = diff(function, x)
print(integrate_function)

p1 = plot(integrate_function, show=False)
p1.show()

function_2 = sin(x)*cos(x)
diff_function_2 = diff(function_2, x)
p2 = plot(diff_function_2, show=False)
p2.show()