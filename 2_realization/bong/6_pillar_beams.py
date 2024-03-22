#https://programmers.co.kr/learn/courses/30/lessons/60061
# 입력값 [x,y,a,b]. 출력값 [x,y,a]
# [x,y]는 보 혹은 기둥의 시작 좌표
# a는 구조물의 종류 0 = 기둥, 1 = 보
# b 는 구조물을 설치 삭제 작성. 0은 삭제, 1은 설치

# 중요
# 기둥은 바닥 혹은 보의 한쪽 끝 부분 혹은 다른 기둥 위에 있어야함
# 보는 한쪽끝이 기둥위에 있거나 양쪽 끝이 다른 보와 동시에 연결되어 있어야함.

#설치 했을 때 문제 없는지 확인
def is_valid(answer):
    for x, y, kind in answer:
        if kind == 0:  # 기둥인 경우
            #바닥면인지, 아래 기둥이 있는지 혹은 좌측에 보가 있는지, 혹은 같은 지점에 보가 있는지 확인
            if y == 0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer:
                continue
            else:
                return False
        elif kind == 1:  # 보인 경우
            #아래 기둥이 있는지, 우측 아래 기둥이 있는지, 좌측과 우측 모두에 보가 있는지
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True

#설치 하는 코드
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        #설계도 소분
        x, y, kind, op = frame
        if op == 1:  # 설치하는 경우
            answer.append([x, y, kind])
            if not is_valid(answer):
                answer.remove([x, y, kind])  # 조건을 만족하지 않으면 삭제
        else:  # 삭제하는 경우
            answer.remove([x, y, kind])
            if not is_valid(answer):
                answer.append([x, y, kind])  # 조건을 만족하지 않으면 다시 추가
    return sorted(answer)


# 테스트
n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 1, 0, 1], [5, 0, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
# build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))
