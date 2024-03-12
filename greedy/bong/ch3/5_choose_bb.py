n, m = map(int,input('N개의 볼링볼, M개의 무게 : ').split())
ball = list(map(int,input('볼링볼 무게 : ').split()))

ans = n * (n-1) / 2

counts = {}
for number in ball:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

result = [count for number, count in counts.items() if count >= 2]

for i in counts.values():
    ans -= i * (i - 1) / 2

print(ans)