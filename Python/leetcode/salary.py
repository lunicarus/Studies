List = [2000,4000,3000,6000,1000]
# minim = max(List)
# maxim = min(List)
# print(sum(List)/len(List))
maximum = 0
minimum = 100000
for n in range(0,len(List)):
    if ((List[n]) > maximum):
        maximum = List[n]
    if ((List[n]) < minimum):
        minimum = List[n]

List.remove(maximum)
List.remove(minimum)
print(sum(List)/len(List))