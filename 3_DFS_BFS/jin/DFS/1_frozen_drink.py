# 1. 문제
# n * m 틀
# 구멍 - 0 , 칸막이 - 1
# 첫 줄 : N, M 길이
# 두 째줄 : N + 1줄까지 틀 형태 주어짐
# 한 번에 만들 수 있는 아이스크림 개수 출력

# 2. 고민한 답안
# 모든 경우의 수 ~ DFS 문제로 풀이
# 0인 노드를 방문하면서 방문한 곳은 1로 바꾸기
# 연결된 그래프 > 카운트 + 1
n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y, graph) :
    # 틀을 벗어나면 False 반환
    if x<=-1 or x>=n or y<=-1 or y>= m:
        return False

    # 현재 위치가 0일때
    if graph[x][y] == 0:
        graph[x][y] = 1 #방문하면서 1로 바꿔줌
        dfs(x -1 ,y, graph)
        dfs(x+1, y, graph)
        dfs(x, y - 1, graph)
        dfs(x, y + 1, graph)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count +=1

print(count)
