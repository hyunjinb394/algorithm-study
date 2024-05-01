#https://www.acmicpc.net/problem/18114
# 10^8무게, 5000개의 물건

# n ,c = map(int,input().split())
# w = list(map(int,input().split()))
n, c = 3,13
w= [3,7,8] 

def check(weights, target_weight, num_items):
    # 물건들의 무게를 오름차순으로 정렬
    weights.sort()

    # 이진 탐색을 사용하여 가능한 조합을 찾음
    left = 0
    right = num_items - 1

    while left <= right:
        mid = left + (right - left) // 2
        # 선택한 물건들의 무게의 합이 목표 무게와 같은지 확인
        if weights[mid] == target_weight:
            return True
        elif weights[mid] < target_weight:
            left = mid + 1
        else:
            right = mid - 1

    return False
for i in range(n):
    if check(w,c,n):
        print(1)
        exit()
print(0)