__author__ = 'Administrator'
from operator import add, mul, floordiv, sub
symbol_table = []
test = '2+13*5'
def calculator(expression):
    assert expression, 'Expression cannot be None!'
    oper = ['+', '-', '*', "/"]
    index = 0
    for item in expression:
        #if item in oper:
        symbol_table.append(item)
        index += 1
    return 0

calculator(test)
print(symbol_table)



