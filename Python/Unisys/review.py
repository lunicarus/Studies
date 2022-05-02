# x = "cat{}".format("s")

# print(f"I have 10 {x}");

import numpy as np
import matplotlib.pyplot as plt

# Y = np.array([2,4,5,6,7,8])
# for x in Y:
#     x = 1/x
#     print(f"{x:.2f}");
    
# X = np.linspace(0,20,100); #Creates an array (n,T,s) from n to T with s elements
# Y = X**2;

# plt.plot(X,Y);
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()


lst = []
for x in range(1,11):
    lst.append(x**2)
    
# print(lst)

items = ["cat","dog","fish"]
# for item in items:
#     print(item)
    
    
# for i,item in enumerate(items):
    # print(f"index:{i} || item : {item}")
    
lst2 = [x**2 for x in range(1,11)]
# print(lst2)

# y = -1/2gt² + v0t;
#marcus and jimmy trhow a ball, m = 10m/s and j = 15m/s, plot the grafic
# v0tm = 10;
# v0tj = 15;
# g = 9.81;
# t = np.linspace(0,2,100);
# ym = -1/2 * g * t**2 + v0tm*t;
# yj = -1/2 * g * t**2 + v0tj*t;

# plt.plot(t,ym)
# plt.plot(t,yj)
# plt.show()


# poem = ["we overthink life",
#         "unknown is the moments unseen",
#         "we believe in light",
#         "but it is in darkness we come to be",
#         "all stars died."
#         ]

# for i,line in enumerate(poem):
#     if "we" in line:
#         print(f"there's a 'we' in the line {i}");
#     else:
#         continue;
# total = 0
# for i in range(10):
#     if not(i%4 == 0) and not(i%6 == 0):
#         total += i;
#         print(total);
#     else:
#         continue;
# a = 1
# b = -5
# c = 6
# x1 = (-b + ( (b**2-4*a*c)**-2 ) )/(2*a)
# x2 = (-b - ( (b**2-4*a*c)**0.5 ))/(2*a)
# t1 = (2*c)/(-b-((b**2-4*a*c)**-2))
# t2 = (2*c)/(-b+((b**2-4*a*c)**-2)) #baskara formulas

# print(f"x1 has the value of: {x1} and x2: {x2}, t1 is {t1} and t2 is {t2}")


# a1 = np.array([2,3,4,5,8,10]);
# print(a1)

# print(a1[a1%4 == 0]) #takes the a1 array, tests if is divisible by 4, returns boolean array, True values becomes index.

# def my_function(*kids):
#   print("The youngest child is " + kids[len(kids)-1])
  
# my_function("jorge","alice","maria","joaquim")


# def my_functio(**kid):
#   print("His last name is " + kid["lname"])
  
# my_functio(fname="jose",lname="silva")

