# 1. 문제
# N : 떡의 개수, M : 요청한 떡의 길이, H : 절단기 높이
# (H - (개별 떡의 높이))의 총합 = M
# 개별 떡 높이는 10억보다 작거나 같은 양의 정수 또는 0

# 2. 고민한 답안 
# 1) 순차탐색
# 순차 탐색 O(N) 으로 풀면 시간이 초과될까 궁금해서 작성
# for문 2개로 N^2에 가까운 시간복잡도.. 

N, M = map(int, input().split())
tteok_height = list(map(int,input().split()))

def sequential_search(tteok_height, M) :

    max_height = 0 # 절단기 최대 높이

    for H in range(max(tteok_height)+1) :
        total = sum(max(0, tteok - H) for tteok in tteok_height )
        if  total  >= M:
            max_height = H
            break
    return max_height

print(sequential_search(tteok_height,M))

# 2) 이진탐색

## 교재풀이 4404ms 
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
ddeoks = list(map(int, sys.stdin.readline().rstrip().split()))


start, end = 0, max(ddeoks)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in ddeoks:
        if i > mid:
            total += i - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)


# 리스트 컴프리핸션 사용
# 시간을 더 줄여보자 2384 ms

import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
ddeoks = list(map(int, sys.stdin.readline().rstrip().split()))

start, end = 0, max(ddeoks)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum([i - mid for i in ddeoks if i > mid]) 

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)


# 3. 더 빠른 답안이 있을까?

import numpy as np
import time

# 테스트 케이스 정의
n, m = 1000000, 2000000000  
ddeoks = np.arange(1, n+1)  

start, end = 0, ddeoks.max()
result = 0

start_time = time.time() 

while start <= end:
    mid = (start + end) // 2
    total = np.sum(ddeoks[ddeoks > mid] - mid)  

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

end_time = time.time() 

print(result)
print(f"실행 시간: {end_time - start_time} 초")

# 0.068 - 0.099 초
# 백준은 np 같은 외부 라이브러리 사용 불가
# time 모듈로 시간 측정

