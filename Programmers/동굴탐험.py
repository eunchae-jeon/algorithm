from collections import deque
def solution(n, path, order):
    path_dict = {i:[] for i in range(n)}
    order_dict = {o[0]:o[1] for o in order}
    block_dict = {o[1]:1 for o in order}
    visited = [0]*n
    for fr, to in path:
        path_dict[fr].append(to)
        path_dict[to].append(fr)
    queue = deque([0])
    visited[0] = 1
    if 0 in block_dict:
        return False
    block_queue = {}
    while queue:
        cur = queue.popleft()
        if cur in order_dict:
            block_dict[order_dict[cur]] = 0
        for p in path_dict[cur]:
            if p not in block_dict or block_dict[p] == 0:
                if visited[p] == 0:
                    visited[p] = 1
                    queue.append(p)
            else:
                block_queue[p] = 1

        
        if not queue:
            new_block = {}
            for b in block_queue.keys():
                if b in block_dict and block_dict[b] == 0:
                    if visited[b] == 0:
                        visited[b] = 1
                        queue.append(b)
                else:
                    new_block[b] = 1
            block_queue = new_block
    if sum(visited) == n:
        answer = True
    else:
        answer = False
    return answer

if __name__ == "__main__":
    # print(solution(9,	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],	[[8,5],[6,7],[4,1]]))
    print(solution(9,	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],	[[4,1],[8,7],[6,5]]	))