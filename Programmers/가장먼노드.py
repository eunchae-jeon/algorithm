from collections import deque
from collections import Counter

def solution(n, edge):
    nodes = [[] for _ in range(n+1)]
    visited = [-1 for _ in range(n+1)]
    for e in edge:
        nodes[e[0]].append(e[1])
        nodes[e[1]].append(e[0])

    queue = deque([1])
    visited[1] = 0
    while queue:
        node = queue.popleft()
        for n in nodes[node]:
            if visited[n] < 0:
                queue.append(n)
                visited[n] = visited[node]+1

    return Counter(visited)[max(visited)]


if __name__ == "__main__":
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))


        

