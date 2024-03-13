n = int(input('동전 갯수 입력 : '))                         #[5개]
coin = list(map(int,input('동전 입력 : ').split()))         #[3 2 1 1 9]

coin.sort()

ans = 1 
for x in coin:
    if ans < x:
        break
    ans += x

print(ans)