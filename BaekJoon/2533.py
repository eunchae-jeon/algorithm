import collections
import sys
In = sys.stdin.readline

def solution():
    n = int(In())
    connect = {}
    parent = {}
    level = {}
    early_adoptor = {}
    visited = {}
    for _ in range(n-1):
        f1, f2 = map(int, In().split())
        visited[f1] = False
        visited[f2] = False
        if f1 not in connect:
            connect[f1] = [f2]
        else:
            connect[f1].append(f2)
        if f2 not in connect:
            connect[f2] = [f1]
        else:
            connect[f2].append(f1)

    queue = collections.deque([(f1, 0)])
    while queue:
        f, lv = queue.popleft()
        if lv not in level:
            level[lv] = [f]
        else:
            level[lv].append(f)
        
        for child in connect[f]:
            if visited[child] == True: continue
            parent[child] = f
            queue.append((child, lv+1))
            visited[child] = True

    keys = sorted(level.keys(), reverse=True)
    for lv in keys:
        for f in level[lv]:
            if f not in early_adoptor:
                early_adoptor[parent[f]] = True
    return len(early_adoptor)

if __name__ == "__main__":
    print(solution())