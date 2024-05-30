# 1. 문제 이해
# union-find 문제

# 2. 문제 풀이

def find_team(team, x) :
    # 자기자신이 아니면 부모 노드 찾음
    if team[x] != x :
        team[x] = find_team(team, team[x])
    return team[x]

def gather_team(team, a ,b) :
    a = find_team(team, a)
    b = find_team(team, b)

    if a < b :
        team[b] = a
    else : 
        team[a] = b

n, m = map(int, input().split())
team = [0] * (n +1)

# 자기 자신으로 초기화
for i in range(0, n+1) :
    team[i] = i

for i in range(m) : 
    first , a, b = map(int, input().split())
    if first == 0 :
        gather_team(team, a, b)
    elif first == 1 :
        if find_team(team, a) == find_team(team, b):
            print("YES")
        else :
            print("NO")