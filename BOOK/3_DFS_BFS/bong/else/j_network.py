#https://school.programmers.co.kr/learn/courses/30/lessons/43162

#dfs 방식을 풀면 될듯

def solution(n, comps):
    state = [False] * n
    ans = 0
    def netw(node):
        stack = [node]
        while stack:
            current = stack.pop()
            if not state[current]:
                state[current] = True
                for i in range(n):
                    if comps[current][i] == 1 and not state[i]:
                        stack.append(i)

    for i in range(n):
        if not state[i]:
            netw(i)
            ans += 1
    return ans

n1 = 3
computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n2 = 3
computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n1, computers1)) 