def org(lang):
    # 문자와 숫자 구분하기 위한 식
    string = ''.join(sorted(''.join(l for l in lang if l.isalpha())))   #   문자로 구분한뒤 sort를 통해서 나열
                                                                        #   ''.join을 통해 list가 아닌 string으로 유지
    number = ''.join(n for n in lang if n.isdigit())                    #   숫자들만 구분
    total_num = sum(int(n) for n in number)                             #   숫자 모두 더함
    return string + str(total_num)
a= 'K1KA5CB7'
print(org(a))