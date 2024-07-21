# 1. 문제
# 1개 이상 단위의 연속된 문자열을 잘라 압축해서 표현
# 표현한 문자열 중 가장 짧은 것의 길이를 return
# s의 길이는 1이상 1000 이하
# s는 알파벳 소문자로만 이루어짐

# 2. 고민한 답안
def compress_string(s, unit):
    compressed = ""
    prev = s[0:unit]
    count = 1
    for i in range(unit, len(s), unit):
        # 현재 부분 문자열
        sub = s[i:i+unit]
        # 이전 문자열과 동일하다면 카운트 증가
        if prev == sub: 
            count += 1
        # 다르다면 압축 문자열에 추가
        else: 
            if count != 1:
                compressed += str(count)
            compressed += prev
            prev = sub
            count = 1

    # 남은 문자열 처리
    if count != 1:
        compressed += str(count)
    compressed += prev
    return compressed

def solution(s):
    # 문자열의 길이가 1이라면 더 이상 압축할 수 없으므로 1을 반환
    if len(s) == 1:
        return 1
    answer = len(s)
    # 1부터 문자열 길이의 절반까지 단위 길이를 늘려가며 압축 길이 탐색
    for unit in range(1, len(s)//2 + 1):
        compressed = compress_string(s, unit)
        answer = min(answer, len(compressed))
    return answer



# 3. 효율적인 답안

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
    'aaaaaa',
]

for x in a:
    print(solution(x))