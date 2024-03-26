# 1. 문제
# 매개변수로 2차원 배열 key와 lock이 주어짐
# 열쇠로 자물쇠를 열 수 있으면 true, 열 수 없으면 false를 return
# key는 M × M(3 ≤M ≤ 20, M은 자연수) 크기 2차원 배열
# lock은 N × N(3 ≤N ≤ 20, N은 자연수) 크기 2차원 배열
# M은 항상 N 이하
# key와 lock의 원소는 0 또는 1로 이루어짐
# 이때 0은 홈 부분, 1은 돌기 부분


# 2. 참고한 답안

# 2차원 배열 90도 회전 메소드
def rotate_by_90deg(matrix):
    n = len(matrix)  # 원래 행렬의 행 길이
    m = len(matrix[0])  # 원래 행렬의 열 길이
    new_matrix = [[0] * n for _ in range(m)]  # 90도 회전한 행렬 초기화

    for i in range(n):
        for j in range(m):
            new_matrix[j][n - 1 - i] = matrix[i][j]  # 원래 행렬을 90도 회전

    return new_matrix  # 회전한 행렬 반환

    
# 3배x3배로 확장된 자물쇠의 가운데 부분 (original 자물쇠)이
# 모두 1인지 (i.e. 열쇠가 맞는 지) 확인
def check(new_lock):
    n = len(new_lock) // 3  # 확장된 자물쇠의 원래 크기

    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False  # 가운데 부분이 모두 1이 아니라면 False 반환
    return True  # 가운데 부분이 모두 1이라면 True 반환

    
# 메인 solution
def solution(key, lock):
    n = len(lock)  # 자물쇠의 크기
    m = len(key)  # 열쇠의 크기
    # 3배 x 3배로 자물쇠 초기화
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠 중간 부분에 기존 자물쇠 값 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]

    # 열쇠가 맞는 지 체크 - 모든 방향에 대해
    for _ in range(4):
        key = rotate_by_90deg(key)  # 열쇠를 90도 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 열쇠 끼워보기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
            # 맞는 지 검사
            if check(new_lock):
                return True
            # 안 맞으면 열쇠 다시 빼기
            for i in range(m):
                for j in range(m):
                    new_lock[x + i][y + j] -= key[i][j]
    return False




# 혁준
# Convolution Neural Network Padding 개념 사용
# CNN에서 이미지 크기 유지를 위해서 padding을 사용하는 것에서 문제풀이 인사이트를 얻음
 
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
import numpy as np

def solution(key, lock):
    N = len(lock)
    M = len(key)

    padded_lock = padding(lock, M-1)

    for _ in range(4):
        for i in range(N+2*(M-1)):
            for j in range(N+2*(M-1)):
                np_key = np.array(key)
                total = padded_lock[i:i+M, j:j+M] + np_key

                # 모든 lock 부분이 1이 되는지 확인
                if np.all(total[M-1:M-1+N, M-1:M-1+N] == 1):  
                    return True
        key = rotate(key)
    return False


def padding(mat, M):
    # mat의 크기
    N = len(mat)
    # 패딩의 크기
    pad_size = N + 2*(M-1)  # 원본 크기 + (상하좌우 각각 M-1개씩 추가)

    # 패딩된 리스트 생성 (전부 0으로 초기화)
    padded_mat = [[0]*pad_size for _ in range(pad_size)]

    # 원본 mat의 내용을 새 리스트의 가운데에 복사
    for i in range(N):
        for j in range(N):
            padded_mat[i+(M-1)][j+(M-1)] = mat[i][j]

    return np.array(padded_mat)

    
def rotate(mat):
    n = len(mat)
    # 시계 방향으로 90도 회전한 행렬을 생성
    # 원래 행렬의 열을 거꾸로 한 순서대로 새 행렬의 행으로 설정
    rotated_mat = [[mat[n-j-1][i] for j in range(n)] for i in range(n)]
    return rotated_mat