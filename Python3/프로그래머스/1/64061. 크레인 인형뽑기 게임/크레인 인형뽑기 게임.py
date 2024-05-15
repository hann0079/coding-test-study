def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []

    for v in moves:
        for i in range(n):
            if board[i][v - 1] != 0:
                if stack and stack[-1] == board[i][v - 1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][v - 1])
                board[i][v - 1] = 0
                break
    return answer
