# n은 10^5이하, m은 10^6 이하
# m개의 a집, b집, 유지비 입력

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

datas = [list(map(int, input().split())) for _ in range(m)]
datas = sorted(datas, key=lambda x: x[2])

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

result, last = 0, 0
for data in datas:
    a, b, cost = data
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
        last = cost

print(result - last)