import sys
import os
import math
from sympy import *
from sympy.parsing.sympy_parser import parse_expr


# difine the symbols you need to use
x , y , z = symbols("x y z")
init_printing(use_unicode=True)

def diffExpr(expr,by,times):
    if type(expr) == type(' '):
        new_expr = parse_expr(expr)
    else:
        new_expr = expr
    for _ in range(0,times):
        new_expr = diff(new_expr , by)

    return new_expr

# expression = input('Enter expression: ')
expression = x**2
diff_by = input('Derivitive by: ')
diff_times = int(input('How many times: '))


print(diffExpr(expression,diff_by,diff_times))
