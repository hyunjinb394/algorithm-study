def strick(n):
    n = str(n)                                  #받은 숫자를 문자열 형식으로 변환(이를 통해 1개씩 개산 할수 있게
    l = int(len(n)/2)                           #길이를 반으로 나눔. 이는 반반 계산해야 하기 때문
    front = sum(int(num) for num in n[:l])      #앞에 숫자 합
    back = sum(int(num) for num in n[l:])       #뒤에 숫자 합

    if front == back:
        return 'LUCKY'
    else:
        return 'READY'

a = '123402'

print(strick(a))