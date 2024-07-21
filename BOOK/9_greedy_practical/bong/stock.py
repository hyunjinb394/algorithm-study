#5초, 256mb

# 뒤에 오는 일수 중 하루라도 너 큰 일수인 날이 있으면 매수 후 가장 큰 일수인 날에 매도
import sys

input = lambda:sys.stdin.readline().rstrip()

#n은 10^6
n = int(input())

for _ in range(n):
    #day는 10^4
    day = int(input())
    price = list(map(int,input().split()))

    ans = 0
    max_price = 0

    for p in reversed(price):
        if p > max_price:
            max_price = p
        ans += max_price - p

    print(ans)

    # while len(price) > 1:
    #     highest = max(price)
    #     highest_day = price.index(highest)
    #     if highest_day != 0:
    #         ans += highest_day * highest - sum(price[:highest_day])
    #         del price[:highest_day]
    #     else:
    #         del price[0]
    # print(ans)
