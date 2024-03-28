#https://www.acmicpc.net/problem/1874
# 문제 설명
# 1부터 n까지의 수가 존재, 이 수들을 순서대로 나열해야함.
# 나열 하기이전에 stack[]이라는 공간에 넣었다 뽑음.
# 뽑아내야 하는 순서는 input에 주어지는 임의의 수열


#코드 순서
#1. stack에 1부터 넣음. 근데 넣을 때 만일 squence에 들어있는 수가 있다면 그수는 제거
#2. 만일 가장 stack 위에있는 수가 지금 빼야 할 숫자보다 클시 'no' 출력(왜냐하면 이건 어짜피 실패하는 코드가 되기 때문) 
# def sol(sequence):
#     operations = []   # 답을 저장하는 공간
#     stack = []        # 스택 공간
#     current = 1       # 현재 넣어야 할 수 변수

#     for num in sequence:
#         # 현재 넣어야 할 수(num)보다 큰 수가 스택에 있는 경우
#         while current <= num:
#             stack.append(current)
#             operations.append('+')
#             current += 1
        
#         # 스택의 맨 위에 있는 수가 현재 수열의 수와 같은 경우
#         if stack[-1] == num:
#             stack.pop()
#             operations.append('-')
#         else:
#             # 스택의 맨 위에 있는 수가 현재 수열의 수와 다른 경우
#             return 'NO'
#     return operations

# n = 8
# sequence1 = [4,3,6,8,7,5,2,1]
# n = 5
# sequence2 = [1,2,5,3,4]

# print(sol(sequence1))


n = int(input())
sequence = [int(input()) for _ in range(n)]


ans = []   # 답을 저장하는 공간
stack = []        # 스택 공간
current = 1       # 현재 넣어야 할 수 변수

for num in sequence:
    # 현재 넣어야 할 수(num)보다 큰 수가 스택에 있는 경우
    while current <= num:
        stack.append(current)
        ans.append('+')
        current += 1
        
        # 스택의 맨 위에 있는 수가 현재 수열의 수와 같은 경우
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
            # 스택의 맨 위에 있는 수가 현재 수열의 수와 다른 경우
        ans =['NO']
        break


for a in ans:
    print(a)