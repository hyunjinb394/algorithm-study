n = int(input("몇명인지 입력: "))
data = list(map(int, input("공포도 입력 : ").split()))

data.sort()
len(data)

ans = 0

while data != []:
    ans = ans + 1
    data = data[data[0] + 1:]


print(ans)