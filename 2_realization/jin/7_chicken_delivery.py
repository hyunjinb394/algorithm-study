# 1. 문제
# A라는 집과 치킨집과의 거리 = A의 치킨거리 
# 도시에 존재하는 모든 집들의 치킨거리를 합한 값 = 도시의 치킨거리
# A의 치킨거리는 치킨집들중에 가장 가까운 치킨집과의 거리
# 치킨집들중에 M개의 치킨집을 제외하고 모두 폐업 예정
# 여러개의 치킨집중 M개의 치킨집을 고르고 그때의 도시의 치킨거리를 구하기

# 2. 고민한 답안
from itertools import combinations
import sys
sys.stdin.readline

graph = []
n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i+1, j+1))
        elif graph[i][j] == 2:
            chicken.append((i+1, j+1))
            
result = n*2 * len(house)
for comb in list(combinations(chicken, m)):
    dist = 0
    for a, b in house:
        temp = n*2
        for x, y in comb:
            temp = min(temp, abs(a-x) + abs(b-y))
        dist += temp
    result = min(result, dist)
        
print(result)


