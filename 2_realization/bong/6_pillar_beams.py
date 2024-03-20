#https://programmers.co.kr/learn/courses/30/lessons/60061

def is_valid(answer):
    for x, y, kind in answer:
        if kind == 0:  # 기둥인 경우
            if y == 0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer:
                continue
            else:
                return False
        elif kind == 1:  # 보인 경우
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, kind, op = frame
        if op == 1:  # 설치하는 경우
            answer.append([x, y, kind])
            if not is_valid(answer):
                answer.remove([x, y, kind])  # 조건을 만족하지 않으면 삭제
        else:  # 삭제하는 경우
            answer.remove([x, y, kind])
            if not is_valid(answer):
                answer.append([x, y, kind])  # 조건을 만족하지 않으면 다시 추가
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))


# 테스트
n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
print(solution(n, build_frame))
