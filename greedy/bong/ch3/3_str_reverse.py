s = input('100만개 이하의 0과 1 입력 : ')

ref_s = '.'

n=0
for i in s:
    if i != ref_s[-1]:
        ref_s = ref_s + i
    else:
        ref_s = ref_s
    n += 1

ref_s = ref_s[1:]

ans = 0
for i in ref_s:
    if i != ref_s[0]:
        ans += 1
    else:
        ans = ans

print(ans)