def solution(my_string):
    answer = ''
    vowel = [ 'a', 'e', 'i', 'o', 'u']
    for m in my_string:
        if m not in vowel:
            answer += m
    return answer