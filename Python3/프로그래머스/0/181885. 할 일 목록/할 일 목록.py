def solution(todo_list, finished):
    result = []
    for i in range(len(todo_list)):
        if not finished[i]:
            result.append(todo_list[i])
    return result