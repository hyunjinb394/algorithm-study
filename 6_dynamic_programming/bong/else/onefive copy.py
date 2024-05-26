def sol(L):
    MOD = 1000_000_009
    if L <= 3:
        ans = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
        return ans[:L]

    ans = [[0, 0, 0] for _  in range(L)]


    ans[0] = [1, 0, 0] 
    ans[1] = [0, 1, 0]
    ans[2] = [1, 1, 1]


    for i in range(3, L):
        ans[i][0] = (ans[i-1][1] + ans[i-1][2]) % MOD
        ans[i][1] = (ans[i-2][0] + ans[i-2][2]) % MOD
        ans[i][2] = (ans[i-3][0] + ans[i-3][1]) % MOD

    return ans


n = int(input())
inp = [int(input()) for _ in range(n)]
large = max(inp)


ans = sol(large)


for i in inp:
    print(sum(ans[i-1]) % 1_000_000_009)