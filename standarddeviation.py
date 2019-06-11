from statistics import mean
import math

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = mean(arr)
num = []
dino = 0

for i in range(0, n):
    num.append((arr[i] - m) * (arr[i] - m))
    dino = i + 1

numm = sum(num)

ans = math.sqrt(numm / dino)

print(ans)


