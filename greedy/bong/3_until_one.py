n, k = map(int,input().split())

ans = 0

while n > k:
    ans = ans + (n%k)
    n = n//k
    ans = ans + 1

if n == k:
    ans = ans
else:
    ans = ans + n - 1

print(ans)