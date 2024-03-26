#https://www.acmicpc.net/problem/5014
# 총 f층, 도착지는 g층에 위치. 강호는 s층에 위치
# u,d는 몇층 위,아래로 갈수 있는지 적혀있음

# 가장 적게 시행되는 경우를 찾아야 하기에 bfs


from collections import deque

def sol(direc):
    f,s,g,u,d = direc
    qu = deque([(s,0)])
    state =[False]*f        #동일한곳 가지 않기위해 생성

    while qu:
        now, ans = qu.popleft()

        if now == g:
            return ans
        
        next = [now + u, now - d]

        for n in next:
            if 1 <= n <= f and not state[n-1]:      #n-1인 이유는 1층이 0에 위치하듯 한개씩 밀림
                state[n-1] = True
                qu.append((n, ans + 1))
    return 'use the stairs'

a1 = [10, 1, 10, 2, 1]
a2 = [100, 2, 1, 1, 0]

sol(a2)