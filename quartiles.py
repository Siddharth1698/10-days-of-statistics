import numpy as np

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
l = []
u = []
length = len(arr)
ll=int(length / 2)
for i in range(0, ll):
    l.append(arr[i])


for i in range(ll+1, n):
    u.append(arr[i])


print(np.median(l))
print(np.median(arr))
print(np.median(u))


