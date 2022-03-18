#Given an integer number n, return the difference between the product of its digits and the sum of its digits. 
#https://www.figma.com/file/Wc8qOkErG6K3FH0wqFOw1J/Untitled
n = 252
tot = 0
mul = 1
sumi = 0
while(n>0):
    digit=n%10
    sumi+=digit
    mul*=digit
    n=n//10
print(mul*sumi)