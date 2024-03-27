# 1. 문제
# 컴퓨터 개수 n
# computers : 2차원 배열, 컴퓨터 연결 정보 
# 네트워크 개수 return 
# n은 1 이상 200 이하
# 연결은 computers[i][j] = 1로 표현

# 2. 고민한 답안
def solution(n, computers):            
    answer = 0
    visited = [0 for i in range(len(computers))]

    def dfs(i):
        visited[i] = 1
        for a in range(n):
            # i가 방문하지 않은 a와 연결되어 있으면 탐색
            if computers[i][a] and not visited[a]:
                dfs(a)      
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
        
    return answer


