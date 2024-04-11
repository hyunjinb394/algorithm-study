# https://www.acmicpc.net/problem/2343
# 시간복잡도 2초, 메모리 제한 128mb
# n개의 강의 => 10^6, m개의 강의 => n개이하, 시간은 10^4분
# 시간 복잡도 3nlogn 간당간당

import sys

n, m = map(int, sys.stdin.readline().split())
lessons = list(map(int, sys.stdin.readline().split()))

def check(bluray_size, lessons, m):
    count = 1
    total_time = 0
    
    for lesson in lessons:                                                                  # 시간복잡도 n
        if total_time + lesson > bluray_size:   #기준 시간보다 크다면
            count += 1                          #블루레이 1개 추가
            total_time = lesson                 #현재 강의 시간 새로운 블루레이에 추가
        else:
            total_time += lesson                #현재 강의 시간 기존 블루레이에 추가
    
    return count <= m

def binary_search(lessons, m):
    start = max(lessons)            # 최소
    end = sum(lessons)              # 최대
    
    result = 0
    
    while start <= end:
        mid = (start + end) // 2    #중앙값
        
        if check(mid, lessons, m):  #이항 정렬          -> logm                             ->결론 시간복잡도 nlogm
            result = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return result

 
answer = binary_search(lessons, m)
print(answer)


