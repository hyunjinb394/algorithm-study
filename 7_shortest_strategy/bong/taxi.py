#https://school.programmers.co.kr/learn/courses/30/lessons/72413
# n은 200이하

import sys

n, s, a, b = 6,4,6,2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

# n=지점 개수 s=출발지점 a=A의 도착지점 b=B의 도착지점 fares=예상택시요금
def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[0 if i == j else INF for j in range(n+1)] for i in range(n+1)]
    
    for i in fares:
        graph[i[0]][i[1]] = i[2]
        graph[i[1]][i[0]] = i[2]
    
    for i in range(1,n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                graph[x][y] = min(graph[x][y], graph[x][i] + graph[i][y])

    answer = graph[s][a] + graph[s][b]
    
    for i in range(1,n+1):
        answer = min(answer, graph[i][a]+graph[i][b]+graph[s][i])
    
    return answer

print(solution(n, s, a, b, fares))