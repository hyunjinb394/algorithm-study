# 1. 문제 이해
# 마일리지 1-36
# 마일리지 많은 순으로 수강인원이 신청되는 방식
# n 과목수, m 마일리지
# pi 신청한 사람 수 ,li : 수강 인원
# 각 사람이 마일리지를 얼만큼 넣었는지

#2. 문제풀이
# 우선순위
# 1) pi < li 인 경우에는 마일리지를 1만 넣기
# 2) pi >= li 인 경우 최소 마일리지(제한인원 수 인덱스 값) 값으로 신청,
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
subject_mileages = []

for _ in range(n):
    p, l = map(int, input().split())
    mileages = list(map(int, input().split()))
    if p < l:
        subject_mileages.append(1)
    else:
        mileages.sort(reverse=True)
        subject_mileages.append(mileages[l-1])

subject_mileages.sort()

get_in = 0
for mileage in subject_mileages:
    if m >= mileage:
        m -= mileage
        get_in += 1
    else:
        break

print(get_in)
