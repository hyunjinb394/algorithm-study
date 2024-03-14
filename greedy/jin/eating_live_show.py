# 1. 문제 & 조건
# N개의 음식을 1번부터 먹기 시작
# 번호 증가 순서대로 음식을 가져다 줌
# 마지막 번호의 음식을 먹으면 1번 음식이 다시 앞으로 옴
# 음식 1개를 1초동한 섭취 후 남은 음식은 두고 다음 번호의 음식 섭취
# 회전판이 음식을 가져오는데 걸리는 시간은 없다고 가정
# 먹방 시작 후 k 초 후 네트워크 장애로 방송 일시 중단, 몇 번 부터 섭취?
# food_times : 각 음식을 모두 먹는데 필요한 시간이 번호 순서대로 들어있는 배열
# k : 방송이 중단된 시간
# 더 섭취해야할 음식이 없으면 -1을 반환

# 2. 고민한 답
from operator import itemgetter

def solution(food_times, k):
    foods = []
    length = len(food_times) 
   
    for i in range(length):
        foods.append([food_times[i], i + 1])
    
    foods.sort()
    
    time = 0
    for i, food in enumerate(foods):
        diff = food[0] - time
        if diff != 0 :
            spend = diff * length
            if spend <= k:
                k -= spend
                time = food[0]

            else: 
                k %= length
                sublist = sorted(foods[i:], key= itemgetter(1) )
                return sublist[k][1]
        n -=1

    return -1

# 3. 효율적인 답
# heap을 이용한 방식

import heapq

def solution(food_times,k):
    if sum(food_times) <= k:
        return -1
    rem_tim = k
    h = [] # 음식들을 넣어줄 heap
    l = len(food_times)

    for i in range(l):
        heapq.heappush(h,(food_times[i],i+1)) # 소요 시간 순서대로 음식들을 minheap에 넣어줌.

    previous = 0 #전 음식 시간 저장
    now = 0 #현재 음식 시간 저장
    
    while (h[0][0] - previous)*l <= rem_tim: #다음 음식을 다 먹어치운 cycle까지 시간이 남았을 때
        now = heapq.heappop(h)[0] #다음 음식을 뽑음
        rem_tim -= (now-previous) * l #남은 시간을 갱신함
        l -= 1 # 남은 음식의 수를 갱신함
        previous = now #지금 먹은 음식을 previous에 저장해줌.
   
    h = sorted(h,key=lambda x:x[1]) #index순서대로 정렬해줌.
   
    return h[rem_tim%len(h)][1]