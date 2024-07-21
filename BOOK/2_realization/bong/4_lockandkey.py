# https://school.programmers.co.kr/learn/courses/30/lessons/60059
# n * n크기의 격자 받아옴
# lock 과 key 비교

import numpy as np

#0으로 둘러쌓인 lock 생성
def make_lock(key, lock):
    #key의 행수와 열수를 받아옴.
    N = len(key)
    M = len(lock)
    #좌,우측에 0 n열 추가
    for row in lock:
        row[:0] = [0] * N
        row.extend([0] * N)
    
    #위,아래 0 n열 추가
    for _ in range(N):
        lock.insert(0, [0] * (M + 2*N))
        lock.append([0] * (M + 2*N))

    return np.array(lock)

#key를 0도, 90도, 180도, 270도로 회전시킨 값을 저장
def lotate_key(key):
    lotated_key = []
    for i in range(4):
        lotated_key.append(np.rot90(key, i))
    return lotated_key



# key = [[0,0,0,0],[1,0,0,0],[0,1,1,0],[0,0,0,0]]
key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

lotate_key(key)
make_lock(key,lock)