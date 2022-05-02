#Write a Python program to split fractional and integer parts of a floating point number
num = 4.9
from audioop import mul
import math
import matplotlib.pyplot as plt
import numpy as np
# def fraction_integer(number):
#     if number % 1 == 0:
#         return (number, 0.0)
#     else:
#         return (number - number%1,number%1)
# print(f"{fraction_integer(num)}")


def sum_natural_numbers(n):
    result = 0
    for n in range(n+1):
        result += n
    return result

def fatoral(n):
    result = 1
    for n in range(1,n+1):
        result *= n
    return result

# x = np.linspace(0,10,1000)
# y = (x**2)
def multiplication():
    n = int(input("inform a number: "))
    M = int(input("inform a multiplier: "))
    return n*M

# plt.plot(x,y);
# # plt.xlabel('x')
# # plt.ylabel('y')
# plt.show()

# print(f"{y:.2f}")

# print(fatoral(4))
def fibonacci(n):
    a = 0
    b = 1
    total = 0
    i = 0
    lst = [1]
    while i < n:
       lst.append(a+b)
       total = a+b
       a=b
       b=total
       i = i+1
    return lst

print(fibonacci(5))
