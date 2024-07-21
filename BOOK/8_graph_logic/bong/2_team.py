# n,m은 10^5 이하.
# 팀을 합침, 같은 팀인지 확인

#n, m
n, m = map(int, input().split())
#팀여부, a학생, b학생
calcu = [list(map(int, input().split())) for _ in range(m)]

parent = [i for i in range(n + 1)]

def find(parent, x):
    if parent[x] !=x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    o, a, b = calcu[i]
    if o == 0:
        union(parent, a, b)
    elif o == 1:
        if find(parent, a) == find(parent, b):
            print('YES')
        else:
            print('NO')





    