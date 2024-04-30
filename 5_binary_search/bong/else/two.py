# https://www.acmicpc.net/problem/2470
# 2*10^9가지 용액 가능, 10^5개의 용액 존재

import sys

n = int(input())
liq = list(map(int,sys.stdin.readline().split()))

#최대 nlogn회 => 5*(10^5)
liq.sort()

ans = [liq[0],liq[n-1]]
tozero = float('inf')

for i in liq:
    if i < 0: break
    for j in reversed(liq):
        if j > 0: break
        if tozero > abs(i+j):
            ans[0] = i
            ans[1] = j
        else:
            break

print(ans[0], ans[1])
