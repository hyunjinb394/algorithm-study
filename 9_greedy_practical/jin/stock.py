# 1. 문제이해
# 주식에 빠져 있는 홍(봉)준이, 어떻게 해야 최대 이익을 얻을 수 있을지 모름
# 홍준이는 매일 세 가지 행동 중 하나를 실행 함
# 주식 사기 / 원하는 만큼 팔기 / 아무것도 안함
# 테스트 케이스 수 T , 날의 수 N : 10^6  

# 2. 문제풀이
# 미래를 알고 있으니 입력된 주가를 거꾸로 파악
# 제일 마지막 주가보다 더 큰 값이 있으면 팔아서 + 이익 
# ex) 1 1 6 3  사고 사고 팔고 아무것도x 
# 더 큰 값이 없으면 제일 큰 값 - 현재 주가 += 총합

import sys

testCases = int(sys.stdin.readline())

for _ in range(testCases):
    # 케이스별 날짜 수
    n = int(sys.stdin.readline())
    price = list(map(int, sys.stdin.readline().split()))
    total_price=0
    max=0

    # 인덱스를 거꾸로 만들기
    # 0,1,2,3 -> 3,2,1,0
    for i in range(len(price)-1,-1,-1):
        if(price[i] > max):
            max = price[i]
        else:
            total_price+=max-price[i]
    print(total_price)



