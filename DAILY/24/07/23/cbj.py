# https://www.acmicpc.net/problem/1436
# 어떤 수에 6이 적어도 3개 이상 있을 경우 
# N은 1e4이하

n = int(input())
#시간복잡도 0(N)회
count = 0
num = 666
while True:
    if '666' in str(num):
        count += 1
        if count == n:
            print(num)
    num += 1


# 0666(0) -> 1666~5666(1~5) -> 6660~6669(0~9) -> 7666~9666(7~9) -> 16660~56669(10~59) -> 66600~66699(00~99) -> 76661~96669(70~99)
# 0(1개)        1~5(5개)         0~9(10개)        7~9(3개)             10~59(50개)          00~99(100개)           71~99(30개)
# 시간복잡도 O(1)회 있을것 같은디... 못찾겠음 ㅠ