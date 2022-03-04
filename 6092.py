slist=list()

for i in range(24):
    slist.append(0)
    
num=int(input())
numlist=input().split()

for i in range(num):
    slist[int(numlist[i])] += 1
    
for i in range(1, len(slist)):
    print(slist[i], end=' ')
