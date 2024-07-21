# 1. 문제
# 컴퓨터 개수 n
# computers : 2차원 배열, 컴퓨터 연결 정보 
# 네트워크 개수 return 
# n은 1 이상 200 이하
# 연결은 computers[i][j] = 1로 표현

# 2. 고민한 답안
from collections import deque

def solution(n, computers):            
    answer = 0
    visited = [0 for i in range(len(computers))]
    
    def bfs(i):
        q = deque()
        q.append(i)
        while q:
            i = q.popleft()
            visited[i] = 1
            for a in range(n):
                if computers[i][a] and not visited[a]:
                     q.append(a)
                
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
        
    return answer
