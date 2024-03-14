# 1. 문제 & 조건
# N * M 형태의 숫자 카드 중 각 행마다 가장 작은 수를 찾는다.
# 그 중에서 가장 큰 수를 찾는다.

# 2. 고민한 방식
n, m = map(int, input().split())

row_card = []
row_min = []


for i in range(n):
        row_card.append(list(map(int,input().split())))
        row_min.append(min(row_card[i]))

answer = max(row_min)

print(answer);


# 3. 더 효율적인 방식
n, m = map(int, input().split())

result = 0

for i in range(n):    
    card = list(map(int, input().split()))    
    min_value = min(card)    
    result = max(min_value, result)    

print(result)

