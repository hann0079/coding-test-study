# 65~90 대문자 97~122 소문자 => 97 - 65 == 32 (알파벳은 26개)
# string 값 수정 불가하므로 list에 넣었다가 join으로 반환
def solution(s):
    flag = True
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            flag = True
            continue
        elif flag and 97 <= ord(s[i]) <= 122:
            s[i] = chr(ord(s[i]) - 32)
        elif not flag and 65 <= ord(s[i]) <= 90:
            s[i] = chr(ord(s[i]) + 32)
        flag = False
    return ''.join(s)