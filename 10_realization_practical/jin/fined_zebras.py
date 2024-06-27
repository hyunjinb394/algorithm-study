# 1. 문제 이해
# 백준 30454번 / 얼룩말을 찾아라! / 브론즈 3
# 연속된 1은 하나로 처리
# 가장 연속된 1이 많은 얼룩말의 검은 줄 수 & 같은 줄 수를 가진 얼룩말들의 수

# 2. 문제 풀이

N, L = map(int, input().split())
gorgeous_zebras = 0
max_stripe = 0

for _ in range(N):
    zebra = input()
    black_line = 0
    in_stripe = False
    
    for i in range(L):
        if zebra[i] == '1':
            if not in_stripe:
                black_line += 1
                in_stripe = True
        else:
            in_stripe = False
    
    if black_line > max_stripe:
        max_stripe = black_line
        gorgeous_zebras = 1
    elif black_line == max_stripe:
        gorgeous_zebras += 1

print(max_stripe, gorgeous_zebras)