#시간 제한 1초, 메모리 제한 128mb
num = int(input())

def form(x):
    n5 = x // 5
    x %= 5
    n3 = x // 3
    x %= 3
    n2 = x // 2
    x %= 2
    return n5 + n3 + n2 +x



print(form(num))
        