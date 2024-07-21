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


# 4. 리스트 컴프리핸션으로 풀어보기

n, m = map(int, input().split())

# 각 행에서의 최소값을 찾아 그 중 최대값을 result에 할당
# 이때 언더스코어(_)는 어떤 특정 값을 무시하기 위한 용도로 사용 
# 언더스코어 사용 시 변수 없이 반복문이 실행됨

result = max([min(map(int, input().split())) for _ in range(n)])

print(result)