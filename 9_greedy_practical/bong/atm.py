# https://www.acmicpc.net/problem/11399
# 시간제한 1초 메모리 제한 256mb

n = int(input())
t = list(map(int,input().split()))

t.sort()

a = 0
b = 0
for i in t:
    a += i
    b += a


print(b)
