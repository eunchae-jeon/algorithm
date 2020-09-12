import sys
import collections
In = sys.stdin.readline

def solution():
    n, m = map(int, In().split())
    cheese = [list(map(int, In().split())) for _ in range(n)]
    total = sum(sum(row) for row in cheese)
    answer = 0
    refresh(cheese, n, m)
    while total > 0:
        visited = [[False] * m for _ in range(n)]
        queue = collections.deque([(0, 0)])
        melt = []
        while queue:
            cur = queue.popleft()
            if cheese[cur[0]][cur[1]] == 1 and isMelting(cur, n, m, cheese):
                melt.append(cur)
                continue
            
            for node in next_nodes(cur, n, m):
                y, x = node
                if not visited[y][x]: 
                    queue.append(node)
                    visited[y][x] = True
        for ch in melt:
            cheese[ch[0]][ch[1]] = 2
            total -= 1
        answer += 1
        refresh(cheese, n, m)
    return answer

def refresh(cheese, n, m):
    queue = collections.deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    ref = []
    while queue:
        cur = queue.popleft()
        ref.append(cur)
        for node in next_nodes(cur, n, m):
            y, x = node
            if (cheese[y][x] == 0 or cheese[y][x] == 2) and not visited[y][x]: 
                queue.append(node)
                visited[y][x] = True
    for cur in ref:
        cheese[cur[0]][cur[1]] = 2


def next_nodes(cur, n, m):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ret = []
    for d in dirs:
        y, x = (cur[0] + d[0], cur[1] + d[1])
        if y >= n or y < 0 or x >= m or x < 0: continue
        ret.append((y, x))
    return ret

def isMelting(cur, n, m, cheese):
    count = 0
    for node in next_nodes(cur, n, m):
        if cheese[node[0]][node[1]] == 2:
            count += 1
    return count > 1

def print_cheese(cheese):
    for c in cheese:
        print(c)
    print()

if __name__ == "__main__":
    print(solution())