import sys
from collections import deque
In = sys.stdin.readline

def solution():
    n = int(In())
    m = int(In())
    dic = {i:[] for i in range(1,n+1)}
    for _ in range(m):
        a, b = map(int, In().split())
        dic[a].append(b)
        dic[b].append(a)
    invite = [0] * n
    queue = deque([(1, 0)]) #num, depth
    while queue:
        person, depth = queue.pop()
        invite[person-1] = 1
        if depth == 2:
            continue
        for friend in dic[person]:
            queue.append((friend, depth+1))

    return sum(invite)-1
    
if __name__ == "__main__":
    print(solution())