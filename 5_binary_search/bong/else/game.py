# https://www.acmicpc.net/problem/1072
# 게임 횟수 10^9회 이하.
# 제한 시간 2초이므로 N회 불가능. 


def additional_games(X, Y):
    Z = (Y * 100) // X
    if Z == 100:
        return -1
    return (X*(Z+1)-100*Y)/(100-(Z+1))
    

# 입력 받기
X, Y = map(int, input().split())

# 결과 출력
print(additional_games(X, Y))
