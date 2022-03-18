low = 3;
high = 7;
# part1 = high//2
# part2 = low//2
# part3 = high%2
# result = part1 - part2 + part3
# print(result)
#encontrar n vezes numeros impares aparecem entre high e low. [3,5,7]
if high%2==0 and low%2==0:
    (high-low)//2
else:
    (high-low)//2+1