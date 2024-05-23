from collections import deque

def solution(info, edges):
    tree = {}
    for e in edges:
        key = e[0]
        val = e[1]
        if key not in tree:
            tree[key] = [val]
        else:
            tree[key].append(val)
    
    for i in range(len(info)):
        if i not in tree:
            tree[i] = []
                
    max_sheep = 0
    q = deque([(0, 1, 0, set())])
    
    while q:
        cur, sheep, wolf, visited = q.popleft()
        max_sheep = max(max_sheep, sheep)
        visited.update(tree[cur])
        
        for n in visited:
            if info[n]: 
                if sheep >  wolf + 1:
                    q.append((n, sheep, wolf + 1, visited - {n}))
            else:
                q.append((n, sheep + 1, wolf, visited - {n}))
    
    return max_sheep