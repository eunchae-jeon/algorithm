from collections import deque
def solution(board):
    n = len(board)
    inf = n*n*600

    best = [[inf]*n for _ in range(n)]
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    queue = deque([(0,0,-1,0)])
    while queue:
        x, y, direc, cost = queue.pop()
        
        for d, (i, j) in enumerate(dirs):
            if direc > 0 and abs(d-direc)==2: continue
            if direc == d or direc == -1:
                n_cost = cost + 100
            else:
                n_cost = cost + 600
            nx, ny = x+i, y+j
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if board[nx][ny] == 0 and best[nx][ny] >= n_cost:
                best[nx][ny] = n_cost
                queue.appendleft((nx, ny, d, n_cost))
    return best[-1][-1]
        

    
#not solved
if __name__ == "__main__":
    # print(solution([[0,0,0],[0,0,0],[0,0,0]]))
    # print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
    
    print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
    # print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
