# https://www.acmicpc.net/problem/18352
# N개의 도시 M개의 단방향 도로, 출발 도시 X, 거리정보 K. 최단 거리인 도시 번호 출력
# 도시의 개수 3e5개, 도로 개수  1e6개
# 메모리 제한 64e6까지가능, 시간은 2초


import sys
input = sys.stdin.readline
INF = int(1e9)

# N=도시개수, M=도로 개수, K=거리정보, X=출발도시번호
N, M, K, X = map(int,input().split())

# 거리 정보
road = [list(map(int,input().split())) for _ in range(M)]


def mem_over_sol(n, k, x, P):
    #9e10의 메모리. 따라서 메모리 부족 뜸 
    graph = [[0 if i==j else INF for j in range(n+1)] for i in range(n+1)]

    # 입력정보로 부터 거리 1로 설정
    for i in P:
        graph[i[0]][i[1]] = 1

    #경로 계산
    for i in range(1,n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])
    
    #답
    for i in range(n+1):
        if graph[x][i] == k: print(i)

# 틀렸는데 왜 틀렸는지 모르겠음
def sol(k,x,P):
    # num으로 끝나는 P 모두 삭제
    def rm(P,num):
        result = [row for row in P if row[1] not in num]
        return result
    # num으로 시작하는 P찾고 도착지만 저장
    def find(P,num):
        result = [row[1] for row in P if row[0] in num]
        return result
    
    #a = 시작점, b = 끝점, d는 거리
    a = [x]
    b = []
    d = 0
    
    while d != k:
        b = find(P,a)
        P = rm(P,b)
        a = b[:]
        d += 1
    
    if len(a) == 0: return [-1]
    else: return a

ans = sol(K, X, road)

for i in ans:
    print(i)
