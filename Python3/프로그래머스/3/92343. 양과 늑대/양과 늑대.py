from collections import deque, defaultdict

def solution(info, edges):
    tree = defaultdict(list)
    for p, c in edges:
        tree[p].append(c)
                
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