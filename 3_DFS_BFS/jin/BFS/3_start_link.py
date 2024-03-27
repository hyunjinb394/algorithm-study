# 1. 문제
# F층 건물, 회사는 G층에 있음
# 현재 S층에 있고 U와 D버튼으로 이동
# U는 위로 U층 이동, D는 아래로 D층 이동
# G층에 도착하기 위해 눌러야하는 최소 버튼 횟수
# 갈 수 없으면 "use the stairs" 출력
# 첫째 줄에 F, S, G, U, D 주어짐

# 2. 고민한 답안
# 방문한 층 기록
# 모든 경로 탐색 후 최소경로 도출 > BFS 

from collections import deque

f, s, g, u, d= map(int, input().split())
# 각 층의 방문 여부 기록
check = [ 0 for _ in range(f+1)]

def bfs():  
    queue = deque()  
    queue.append(s)  

    # 현재 층을 방문으로 표시
    check[s] = 1  

    while queue:  
        y = queue.popleft()  

        if y == g:  
            # 시작 층을 1로 표시했기 때문에 버튼 누른 수는 -1
            return check[y] - 1  
        else:  
            for x in (y - d, y + u):  
                # 유효범위 & 방문하지 않은 층
                if 0 < x <= f and check[x] == 0:  
                    check[x] = check[y] + 1  
                    queue.append(x)  

    return "use the stairs"  


print(bfs())
