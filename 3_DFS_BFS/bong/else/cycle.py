#https://www.acmicpc.net/problem/10451
#재귀 함수 사용하면 좋을것으로 생각

t = 2
n1 = 8
n1_list = [3, 2, 7, 8, 1, 4, 5, 6]
n2 = 10
n2_list = [2, 1, 3, 4, 5, 6, 7, 9, 10, 8]

def cycle(a,list,ans,check):
    if check[a]: ans += 1
    else:
        check[a] = True
        ans = cycle(a,list,ans,check)
    return ans
    
def sol(n,list):
    check = [False] * n
    ans = 0
    for i in range(n):
        if not check[i]:
            cycle(i,list,ans,check)
    return ans

# def cycle(node, graph, visited):
#     visited[node] = True
#     next_node = graph[node]
#     if visited[next_node]:  # 이미 방문한 노드에 도달했을 때
#         return 1  # 사이클의 길이를 반환
#     return 1 + cycle(next_node, graph, visited)  # 재귀적으로 사이클의 길이를 찾음

# def sol(n, lst):
#     graph = [0] + lst  # 인덱스를 1부터 사용하기 위해 0 추가
#     visited = [False] * (n + 1)
#     cycle_lengths = []  # 각 사이클의 길이를 저장할 리스트
#     for i in range(1, n + 1):
#         if not visited[i]:
#             cycle_lengths.append(cycle(i, graph, visited))
#     return len(cycle_lengths)  # 사이클의 개수를 반환


print(sol(n2,n2_list))

