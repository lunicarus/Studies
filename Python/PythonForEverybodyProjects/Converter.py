import numpy as np

def my_trig_sum(a, b):
    """
    function to demo return multiple
    author
    date
    """
    out1 = np.sin(a) + np.cos(b)
    out2 = np.sin(b) + np.cos(a)
    return out1, out2

# a,b = my_trig_sum(2,3)

# print(a)

def convertor(operacoes=[0],resultado = False):
    print(resultado)
    print(operacoes)
    
def board(n):
    zeros = np.zeros(n,n)
    ones = np.ones(n,n)
    