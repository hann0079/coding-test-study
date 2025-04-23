def solution(my_string, alp):
    answer = my_string
    for i in range(len(my_string)):
        if my_string[i]==alp:
            answer=answer[:i]+my_string[i].upper()+answer[i+1:]
    return answer