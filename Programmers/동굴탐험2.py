from collections import deque
def solution(n, path, order):
    path_dict = {i:[] for i in range(n)}
    order_dict = {}
    for o in order:
        order_dict[o[0]] = [o[1]]
        if o[1] == 0:
            return False
    visited = [0]*n
    for fr, to in path:
        path_dict[fr].append(to)
        path_dict[to].append(fr)
    queue = deque([0])
    visited[0] = 1
    while queue:
        cur = queue.popleft()
        for p in path_dict[cur]:
            if visited[p] == 0:
                visited[p] = 1
                queue.append(p)
                try:
                    order_dict[cur].append(p)
                except:
                    order_dict[cur] = [p]

    visited = [0]*n
    visited[0] = 1
    stack = deque([[0, visited[:]]])
    while stack:
        cur, visit = stack.pop()
        visit[cur] = 1
        if cur in order_dict:
            for p in order_dict[cur]:
                if visit[p] == 1:
                    return False
                stack.append((p, visit[:]))
    return True

if __name__ == "__main__":
    print(solution(9,	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],	[[8,5],[6,7],[4,1]]))
    print(solution(9,	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],	[[4,1],[8,7],[6,5]]	))