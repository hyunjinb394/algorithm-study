# num = list(map(int,input("숫자 입력 : ").split()))
# print(num)
num = input("숫자 입력 : ")
ans = 0

for i in num:
    a = int(i)
    if a == 0 or a==1 or ans == 0 or ans == 1:
        ans = ans + a
    else:
        ans = ans * a

print(ans)