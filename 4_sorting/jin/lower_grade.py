# 1. 문제 
# n : 학생 수 ,  1 ≤ N ≤ 100,000 
# A : 학생 이름, B : 학생 성적 AB는 100 이하의 자연수
# 모든 학생의 이름을 성적 낮은 순으로 출력

# 2. 고민한 답안
# 튜플 사용

# N = int(input())
# student_info = [(input().split()[0], int(input().split[1])) for _ in range(N)]
# sorted_data = sorted(student_info, key=lambda x : x[1])

# for student in sorted_data:
#     print(student[0], end=' ')


# 3. 효율적인 답안 (0.00105 초 / 0.07815 MB)
# 이름과 성적 입력받는 부분을 문제 조건에 맞게 수정

import time
import psutil
import os

def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024) 

start_time = time.time()
start_memory = memory_usage()

N = 3
student_info = [("a", "12"), ("b", "23"), ("c", "34")]

N = int(input())
student_info = [tuple(input().split()) for _ in range(N)]
sorted_data = sorted(student_info, key=lambda x: int(x[1]))

for student in sorted_data:
    print(student[0], end=' ')


# 4. 코드 피드백
# 봉준 0.001014초 > 형수 0.001036초 > 현진 0.00105초 > 혁준 0.001140초 
# 공간복잡도 모두 동일 0.0078125 MB
# 리스트 컴프리헨션을 사용해서 데이터 처리가 더 빠른 것으로 보임


# 형수
# n = int(input())
# n = 3
# input_data = [("a", "12"), ("b", "23"), ("c", "34")]

# array=[]
# for i in range(n):
# #   input_data = input().split()
#   array.append((input_data[0], int(input_data[i][1])))
# array = sorted(array, key = lambda student: student[1])
# for student in array:
#   print(student[0], end = ' ')


# 혁준 
# n = int(input())
# n = 3
# input_data = [("a", "12"), ("b", "23"), ("c", "34")]
# grade = []

# for i in range(n):
#     # input_data = input().split()
#     grade.append((input_data[i][0], int(input_data[i][1])))

# grade = sorted(grade, key=lambda student: student[1])

# for student in grade:
#     print(student[0], end=" ")


# 봉준

# n = int(input("학생 수: "))
# nlist = [input().split() for _ in range(n)]

# n = 3
# nlist = [("a", "12"), ("b", "23"), ("c", "34")]

# # lamda는 sorted()함수의 변수를 설정해줌. 변수를 key가 배열x의[1]에 해당한다고 표기함으로서 아래처럼 사용가능.
# nlist = sorted([[l[0],int(l[1])] for l in nlist],key = lambda x: x[1])

# print(nlist)



# 메모리 사용량과 종료 시간 측정
# end_time = time.time()
# end_memory = memory_usage()

# 결과 출력
# print("실행 시간: {:.6f} 초".format(end_time - start_time))
# print("메모리 사용량:", end_memory - start_memory, "MB")