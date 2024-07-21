#떡 갯수 10^6개, 길이 2*10^9개 시간 제한 2초
#길이 관련해서는 시간복잡도 logm만 가능
#떡 갯수는 2nlogn 간당간당

import sys
import numpy as np

# n, m = map(int, sys.stdin.readline().rstrip().split())
# ddeoks = list(map(int, sys.stdin.readline().rstrip().split()))

# 현진 => 고침
def h_ans(m,ddeoks):
    ddeoks = np.array(ddeoks,dtype=np.float64)
    start = 0
    end = ddeoks.max()

    result = 0
    while start <= end:
        mid = (start + end) // 2                                #여기서 문제 발생. => numpy는 효율을 위해서 데이터가 저장되는 bit를 지정함. 
        total = np.sum(ddeoks[ddeoks > mid] - mid)              # 일반적으로는 32bit로 저장. 하지만 이 문제는 4*10^9까지의 숫자가 나올수 있음
                                                                # 따라서 32bit가 커버할 수 있는 데이터 값 이상이 나오면 overflow 발생. 
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


#봉준 = 책 풀이(에 약간 추가)
def ans1(m,dlist):
    start =0
    end = max(dlist)

    while (start <= end):                   #logm회
        total = 0
        mid = (start+ end)//2
        for x in dlist:                     #n회            ->nlogm회
            if x > mid:
                total += x -mid

        if total < m:
            end = mid -1

        #elif를 추가함. 이를 사용하지 않았다면 어떤 경우에도 nlogm회 실행. 하지만 이경우를 추가하는 경우 nlogm회 이전에 끝날수 있음. 하지만 최악의 약1.5배 길어질수도
        elif total == m:
            result = mid
            return result

        else:
            result = mid
            start = mid + 1

    return result 
#봉준 변형(리스트 컴프리헨션)
def ans2(m,dlist):
    start =0
    end = max(dlist)

    while (start <= end):                   #logm회
        total = 0
        mid = (start+ end)//2

        total = sum(x - mid for x in dlist if x > mid)

        if total < m:
            end = mid -1

        #elif를 추가함. 이를 사용하지 않았다면 어떤 경우에도 nlogm회 실행. 하지만 이경우를 추가하는 경우 nlogm회 이전에 끝날수 있음. 하지만 최악의 약1.5배 길어질수도
        elif total == m:
            result = mid
            return result

        else:
            result = mid
            start = mid + 1

    return result 


#기존 혁준
def solution_ricecake1(M, r_list):
    end = max(r_list)
    start = 0
    result = 0

    while (start <= end):
        mid = (start+end)//2
        total = 0
        
        for r in r_list:
            if r - mid > 0:
                total += r-mid

        if total >= M:
            result = mid
            start = mid+1

        if total < M:
            end = mid-1
    return result

#변형 혁준 = (책풀이)
def solution_ricecake2(M, r_list):
    end = max(r_list)
    start = 0
    result = 0

    while (start <= end):
        mid = (start+end)//2
        total = 0
        
        for r in r_list:
            if r - mid > 0:
                total += r-mid

        if total >= M:
            result = mid
            start = mid+1

        else:
            end = mid-1
    return result


import random
import time

n, m = 1000000, 2333
tlist = random.choices(range(1, 2000000001), k=1000000)
# n, m = 4,6
# tlist = [19,15,10,17]

h_time1= time.time()
print(h_ans(m,tlist))
h_time2= time.time()
print('현진 시간:', h_time2 - h_time1)


# j_time1= time.time()
# print(solution_ricecake1(m,tlist))
# j_time2= time.time()
# print('혁준1 시간:', j_time2 - j_time1)

j_time1= time.time()
print(solution_ricecake2(m,tlist))
j_time2= time.time()
print('혁준2 시간:', j_time2 - j_time1)


# b_time1= time.time()
# print(ans1(m,tlist))
# b_time2= time.time()
# print('봉준1 시간:', b_time2 - b_time1)

b_time1= time.time()
print(ans2(m,tlist))
b_time2= time.time()
print('봉준2 시간:', b_time2 - b_time1)