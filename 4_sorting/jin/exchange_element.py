# 1. 문제
# N : 두 배열의 원소 개수 K : 바꿔치기 최대 횟수
# K번의 바꿔치기 연산을 통해 A의 모든 원소의 최댓값을 출력
# N < 100,000 nlogn 설계 가능

# 2. 고민한 답안 (시간 0.001초 / 메모리 0.0078 MB)

import time
import psutil
import os

def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024) 



N, K = map(int, input().split())

# A 배열의 가장 작은 원소 <-> B 배열의 가장 큰 원소
# A 오름차순, B 내림차순

A = list(map(int, input().split()))
B = list(map(int, input().split())) 

# start_time = time.time()
# start_memory = memory_usage()

A.sort()
B.sort(reverse=True)

for i in range(K) :
    if A[i] < B[i] :
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))

# end_time = time.time()
# end_memory = memory_usage()

# print("시간 :", end_time-start_time)
# print("메모리 사용량:", end_memory - start_memory, "MB")

