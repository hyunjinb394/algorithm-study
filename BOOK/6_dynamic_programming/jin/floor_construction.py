# 1. 문제 이해
# 2 * n 바닥에 1*2, 2*1, 2*2로 덮음
# 796796으로 경우의 수 나눔


# 2. 문제 풀이
# n = 1 -> 1
# n = 2 -> 3
# n = 3 -> 5
# 핵심은 점화식 찾기

import sys
n = int(sys.stdin.readline().strip())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1] + 2*d[i-2]) % 796796

print(d[n])

