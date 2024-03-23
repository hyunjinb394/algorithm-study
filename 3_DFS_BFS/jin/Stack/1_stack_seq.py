# 1. 문제
# 스택에 push하는 순서는 반드시 오름차순을 지킴
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 여부
# 만들 수 있다면 push(+)와 pop(-) 연산 수행 순서 출력 
# 만들 수 없으면 NO 출력

# 2. 고민한 답안 (메모리 32704 KB / 시간 4036 ms)
n = int(input())
temp = True
stack = []
result = []
count = 1 # 현재 수

for _ in range(n):
    num = int(input()) 
    while count <= num :
        stack.append(count)
        result.append('+')
        count += 1

    if stack[-1] == num :
        stack.pop()
        result.append('-')
    
    else :
        temp = False
        break

if temp == False :
    print('NO')
else :
    for i in result :
        print(i)

# 함수형으로 작성
        
def is_stack_val(n, numbers):
    temp = True
    stack = []
    result = []
    count = 1 

    for num in numbers : 
        while count <= num :
            stack.append(count)
            result.append('+')
            count += 1

        if stack[-1] == num :
            stack.pop()
            result.append('-')
        else :
            temp = False
            break

    if temp == False :
        return 'NO'
    else :
        return '\n'.join(result)

if __name__ == "__main__" :
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    print(is_stack_val(n, numbers))



# 3. 효율적인 답안

import sys

def solution():
    # sys.stdin.buffer.read().splitlines() : 입력을 한 번에 받아옴
    # input()을 여러번 호출하는 것보다 효율적
    n, *nums = map(int, sys.stdin.buffer.read().splitlines())
    s = []
    answer = []
    cur = 1
    for value in nums:
        while cur <= value:
            answer.append('+')
            s.append(cur)
            cur += 1
        if s.pop() != value:
            return "NO"
        answer.append('-')
    # for문 돌지 않고 join으로 한 번에 출력함
    return '\n'.join(answer)


print(solution())