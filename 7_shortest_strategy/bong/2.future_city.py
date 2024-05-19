# 제한시간 1초, 메모리 128mb
# N은 회사 개수, M은 경로의 개수(1~100개)
# 1번 출발 K 이후 , X 방문 

n, m = map(int, input().split())
path = [list(map(int, input().split())) for _ in range(m)]
x, k = map(int, input().split())

INF = int(1e9)

def book_sol(path, k, x, n):
    # graph의 행은 각 노드를, 열은 그 노드가 열의 노드까지 걸리는 거리를 나타냄
    graph = [[INF]*(n + 1) for _ in range(n + 1)]
    
    #리스트 컴프리핸션 사용. 자신의 거리는 0으로 설정
    graph = [[0 if i == j else graph[i][j] for j in range(n + 1)] for i in range(n + 1)]

    #a에서 b로 가는 거리 1로 설정
    for i in path:
        graph[i[0]][i[1]] = 1
        graph[i[1]][i[0]] = 1

    # a와 b는 a에서 b로 갈때의 변수, i는 중간 지점을 통해서 갈수 있는지 확인 후 최소 길이로 저장
    for i in range(1,n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

    ans = graph[1][k] + graph[k][x]
    if ans >= INF:
        return -1

    else: return ans
    

print(book_sol(path,k,x,n))

