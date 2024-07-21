import sys
import math

# input = sys.stdin.readline
# X,Y = map(int, input().split())

X,Y = 1_000_000, 898_989

#봉준
def bong(X, Y):
    Z = (Y * 100) // X
    if Z == 100 or Z == 99:
        return -1
    return math.ceil((X*(Z+1)-100*Y)/(100-(Z+1)))

#형수
def hung(x,y):
    z = (y * 100) // x

    # 승률이 100%일 때는 더 이상 승률을 변화시킬 수 없으므로 -1 출력
    if z >= 99:
        return -1
    else:
        # 이분 탐색으로 최소 게임 수 찾기
        left, right = 0, 1000000000  # 게임 횟수의 최대 범위 설정
        while left < right:
            mid = (left + right) // 2
            new_z = ((y + mid) * 100) // (x + mid)
            if new_z > z:
                right = mid
            else:
                left = mid + 1
        return left

#혁준
def huck(X,Y):
    Z = (Y * 100) // X

    start, end = 1, 1_000_000_000
    result = -1

    while start <= end:
        mid = (start+end)//2
        newZ = ((Y + mid) * 100) // (X + mid)

        if newZ > Z:
            result = mid
            end = mid - 1
        elif newZ == Z:
            start = mid + 1

    return result

import time

now = time.time()
for i in range(10000):
    bong(X,Y)
end = time.time()
print("bongtime ",(end-now)*10_000)

now = time.time()
for i in range(1000):
    huck(X,Y)
end = time.time()
print("hucktime ",(end-now)*10_000)

now = time.time()
for i in range(1000):
    hung(X,Y)
end = time.time()
print("hungtime ",(end-now)*10_000)

