from collections import deque

def solution(cards1, cards2, goal):
    
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
    
    return "Yes" if not goal_q else "No"