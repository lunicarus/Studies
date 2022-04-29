# x = "cat{}".format("s")

# print(f"I have 10 {x}");

import numpy as np
import matplotlib.pyplot as plt

# Y = np.array([2,4,5,6,7,8])
# for x in Y:
#     x = 1/x
#     print(f"{x:.2f}");
    
X = np.linspace(0,20,100); #Creates an array (n,T,s) from n to T with s elements
Y = X**2;

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
    
lst2 = [x*2 for x in range(1,11)]
print(lst2)