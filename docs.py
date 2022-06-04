import sys
import os
import math
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

# difine the symbols you need to use
x , y , z = symbols("x y z")
init_printing(use_unicode=True)


expr = cos(x**2) + 1
# expr.subs(x,y)


# expr = sqrt(8)
# expr.evalf()

print(pi.evalf(100))

# diff by x
print(diff(expr,x))
# diff 2 times by x
print(diff(expr,x,x))
# diff 2 times by x and then by y
print(diff(expr,x,x,y))

# integrate the expression by x from zero to infinity
print(integrate(expr , (x,0,oo)))

# Limits
# evaluate the limit of an expression when x going to zero from the positive side
limit(expr , x , 0 , '+')

# Series Expansion
# transforming an expression to a 4 expression series
expr = exp(sin(x))
expr.series(x,0,4)

expr.series(x,0,4).removeO()


# Finite differences
f , g = symbols("f g" , cls=Function)
differentiate_finite(f(x)*g(x))

f = Function('f')
dfdx = f(x).diff(x)
print(dfdx.as_finite_difference())


# Equations
Eq(x,y)


# solve the equation x^2=1 for x
solveset(Eq(x**2,1),x)


# Printing
# for using latex
expr1 = integrate(x**2,x)
expr2 = Integral(x**2,x)
print(latex(sqrt(2)))
print(latex(Eq(expr1,y)))
print(latex(expr2))

# for using unicode
pprint(Integral(sqrt(1/x), x), use_unicode=True)

# Parsing
str_expr = 'x**2'
new_expr = parse_expr(str_expr)
print(diff(new_expr))


