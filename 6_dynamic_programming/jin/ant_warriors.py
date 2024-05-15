# 1. 문제 이해
# 홀수 또는 짝수의 창고의 식량의 합 중에 더 많은 값 리턴

# 2. 문제 풀이

import sys
n = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])