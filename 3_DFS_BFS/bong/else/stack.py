#https://www.acmicpc.net/problem/1874
#

n = 8
sequence = [4,3,6,8,7,5,2,1]
operations = []

stack = []        # 스택 초기화
current = 1       # 현재 넣어야 할 수

for num in sequence:
    # 현재 넣어야 할 수(num)보다 큰 수가 스택에 있는 경우
    while current <= num:
        stack.append(current)
        operations.append('+')
        current += 1
    
    # 스택의 맨 위에 있는 수가 현재 수열의 수와 같은 경우
    if stack[-1] == num:
        stack.pop()
        operations.append('-')
    else:
        # 스택의 맨 위에 있는 수가 현재 수열의 수와 다른 경우
        print('NO')
        exit(0)

# 연산 기록 출력
for op in operations:
    print(op)