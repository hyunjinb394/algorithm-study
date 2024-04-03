# 1. 문제
# 컴퓨터 개수 n
# computers : 2차원 배열, 컴퓨터 연결 정보 
# 네트워크 개수 return 
# n은 1 이상 200 이하
# 연결은 computers[i][j] = 1로 표현


# 2. 고민한 답안 (시간 0.5 ms/ 메모리 0.00390625 MB)
import time
import psutil
import os

def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024) 

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
            # 네트워크 개수 +1
            answer += 1
        
    return answer



# 3. 팀원 풀이

# 봉준 (시간 1 ms/ 메모리 0.00390625 MB)
# 스택 사용

def solution(n, comps):
    def netw(node):
        stack = [node]
        while stack:
            current = stack.pop()
            if not state[current]:
                state[current] = True
                for i in range(n):
                    if comps[current][i] == 1 and not state[i]:
                        stack.append(i)

    state = [False] * n
    ans = 0
    for i in range(n):
        if not state[i]:
            netw(i)
            ans += 1
    return ans



# 형수 (시간 0.61 ms/ 메모리 0.00390625 MB)
# 스택 사용

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def bfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            bfs(computers, visited, i)
            answer +=1
        i+=1
    return answer


# start_time = time.time()
# start_memory = memory_usage()

# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

# result = solution(n, computers)

# # 메모리 사용량과 종료 시간 측정
# end_time = time.time()
# end_memory = memory_usage()

# # 결과 출력
# print("네트워크 개수:", result)
# print("실행 시간: {:.6f} 초".format(end_time - start_time))
# print("메모리 사용량:", end_memory - start_memory, "MB")
