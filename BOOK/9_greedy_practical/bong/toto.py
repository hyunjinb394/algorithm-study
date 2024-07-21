# https://www.acmicpc.net/problem/12018
# 시간제한 1초 메모리 제한 256mb

# 첫줄 과목수(n), 마일리지(m)
# 과목마다 2줄, 신청한 사람수(P)와 수강인원(L)
# 이후 얼마나 각각 얼마나 마일리지 넣었는가
import sys

input = lambda:sys.stdin.readline().rstrip()
#n은 수업수, m은 마일리지
n, m = map(int, input().split())

mile = []

#p는 수강신청한 인원수, l은 수강 가능 인원
for _ in range(n):
    p, l = map(int, input().split())
    point = list(map(int, input().split()))
    if p < l:
        mile.append(1)
    else:
        point.sort(reverse=True)
        mile.append(point[l-1])


mile.sort()

c = 0
total_mile = mile[0]

if sum(mile) <= m:
    c = n
else:    
    while total_mile <= m:
        c += 1
        total_mile += mile[c]
print(c)
