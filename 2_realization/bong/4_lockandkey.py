# n * n크기의 격자 받아옴
# lock 과 key 비교

def check(key, lock):
    print(key+lock)

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

check(key,lock)