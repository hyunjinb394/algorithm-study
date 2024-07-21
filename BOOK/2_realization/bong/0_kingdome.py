def move(xy):
    # 좌표를 x좌표와 y좌표 형식으로 변경
    x = xy[0]
    y = int(xy[1])

    ans = 8
    
    # 좌측 혹은 우측에 딱 달라붙었을 때는 반밖에 못감. 1칸 띄워져 있을때는 0.75배 밖에 못감. 이후는 상관 없음
    if x == 'a' or x == 'h':
        ans /= 2
    elif x == 'b' or x == 'g':
        ans *= 0.75

    # y축역시 마찬가지
    if y == 1 or y ==8:
        ans /= 2
    elif y == 2 or y == 7:
        ans *= 0.75
    
    return ans


xy= 'c4'

print(move(xy))