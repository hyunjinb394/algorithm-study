#https://www.acmicpc.net/problem/18114
# 10^8무게, 5000개의 물건

# n ,c = map(int,input().split())
# w = list(map(int,input().split()))
n, c = 3,13
w= [3,7,8] 

def check(weights, target_weight):
    # 물건들의 무게를 오름차순으로 정렬
    weights.sort()
    all = 0

    while all < target_weight:
        for i in weights:
            all += i
            if all == target_weight:
                return 1
        return 0
    