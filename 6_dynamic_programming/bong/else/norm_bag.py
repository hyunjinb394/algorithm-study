# 물품수 N은 1에서 100사이
# 버틸수 있는 무게 K는 1에서 100,0000사이. 
# 각 물건의 무게 W는 1에서 100,000사이.
# 물건의 가치 V는 0에서 1,000사이

n, k = map(int, input().split())
stuffs = [list(map(int, input().split())) for _ in range(n)]

# def sol(N,K,X):
#     li = [0]*N
#     for i in X:
