# https://www.acmicpc.net/problem/2470
# 2*10^9가지 용액 가능, 10^5개의 용액 존재

import sys

n = int(input())
liq = list(map(int,sys.stdin.readline().split()))

#최대 nlogn회 => 5*(10^5)
liq.sort()

left = 0
right = n-1
ph = float('inf')

while left < right:
    check = liq[left]+liq[right]
    if abs(ph) > abs(check):
        ph = check
        ans_left = liq[left]
        ans_right = liq[right]
    
    if check > 0:
        right -= 1
    elif check < 0:
        left += 1
    else: break

print(ans_left,ans_right)    
