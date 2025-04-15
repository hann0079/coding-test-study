def solution(my_string):
    result = ""
    for s in my_string:
        if s.isupper():
            result += s.lower()
        else:
            result += s.upper()
    return result