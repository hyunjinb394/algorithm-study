n = int(input("몇명인지 입력: "))
data = list(map(int, input("공포도 입력 : ").split()))

data.sort(reverse=False)

ans = 0

while data != []:
    ans += 1
    data = data[data[0] + 1:]

    if len(data) == 0:
        break
    elif len(data) < data[0]:
        ans -= 1
    else: continue

print(ans)