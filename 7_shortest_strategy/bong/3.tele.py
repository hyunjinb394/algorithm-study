# 제한시간 1초, 메모리 128mb
# N개의 도시(3*10^4), X에서 Y로 전보 보냄. 통신은 단방향(2*10^5)
# C 도시에서 전보 보낼시 받는 도시 개수와 시간

#n=도시 수, m=통로수, c=전보 도시명
n, m, c = map(int,input().split())
# 통로 경로 및 걸리는 시간
path = [list(map(int,input().split())) for _ in range(m)]

INF = int(1e9)

# N은 도시수, P는 경로, C는 찾는 도시
def sol(N ,P, C):

    #초기 시간 설정
    graph = [[0 if i==j else INF for j in range(N+1)] for i in range(N+1)]

    #입력값을 통해 직접적인 값은 입력
    for i in P:
        graph[i[0]][i[1]] = i[2]

    #경로 입력
    for i in range(1,N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

    #정답 찾기
    number = 0
    time = 0
    for i in graph[C]:
        if i != 0 and i < INF:
            number += 1
            time = max(time, i)
    return [number, time]

ans = sol(n, path, c)
print(ans[0], ans[1])