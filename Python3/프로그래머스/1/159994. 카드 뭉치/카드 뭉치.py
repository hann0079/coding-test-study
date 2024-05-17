from collections import deque

def solution(cards1, cards2, goal):
    answer = "Yes"
    
    cards1_q = deque(cards1)
    cards2_q = deque(cards2)
    goal_q = deque(goal)
    
    while goal_q:
        if cards1_q and goal_q[0] == cards1_q[0]:
            cards1_q.popleft()
            goal_q.popleft()
        elif cards2_q and goal_q[0] == cards2_q[0]:
            cards2_q.popleft()
            goal_q.popleft()
        else:
            break
    
    if goal_q:
        answer = "No"
    
    return answer

if __name__ == '__main__':
    print(solution(	["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
    print(solution(	["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
    print(solution(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], ["string", "or", "integer"], ["string", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]))
