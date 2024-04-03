# 1. 문제 
# n : 학생 수 ,  1 ≤ N ≤ 100,000 
# A : 학생 이름, B : 학생 성적 AB는 100 이하의 자연수
# 모든 학생의 이름을 성적 낮은 순으로 출력

# 2. 고민한 답안
# 튜플 사용

N = int(input())
student_info = [(input().split()[0], int(input().split[1])) for _ in range(N)]
sorted_data = sorted(student_info, key=lambda x : x[1])

for student in sorted_data:
    print(student[0], end=' ')


# 3. 효율적인 답안
# 이름과 성적 입력받는 부분을 문제 조건에 맞게 수정

N = int(input())
student_info = [tuple(input().split()) for _ in range(N)]
sorted_data = sorted(student_info, key=lambda x: int(x[1]))

for student in sorted_data:
    print(student[0], end=' ')
