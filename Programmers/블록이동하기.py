from collections import deque
def solution(board):
    N = len(board)
    board = [[1]*(N+2)] + [[1] + line + [1] for line in board] + [[1]*(N+2)]
    visited = {}
    queue = deque([(1, 1, 0, 0)])
    visited[(1, 1, 0)] = True
    while queue:
        x, y, direction, time = queue.popleft()
        dx, dy = 0, 0
        if direction == 0:
            dx = 1
        else:
            dy = 1
        if (x == N and y == N) or (x+dx == N and y+dy == N):
            return time
        new_pos = []
        # print(board[y][x], board[y+dy][x+dx])
        if direction == 0:
            if board[y][x+2] == 0:
                new_pos.append((x+1, y, 0))
            if board[y][x-1] == 0:
                new_pos.append((x-1, y, 0))
            if board[y+1][x] == 0 and board[y+1][x+1] == 0:
                new_pos.append((x, y, 1))
                new_pos.append((x+1, y, 1))
                new_pos.append((x, y+1, 0))
            if board[y-1][x] == 0 and board[y-1][x+1] == 0:
                new_pos.append((x, y-1, 1))
                new_pos.append((x+1, y-1, 1))
                new_pos.append((x, y-1, 0))
        else:
            if board[y+2][x] == 0:
                new_pos.append((x, y+1, 1))
            if board[y-1][x] == 0:
                new_pos.append((x, y-1, 1))
            if board[y][x+1] == 0 and board[y+1][x+1] == 0:
                new_pos.append((x, y, 0))
                new_pos.append((x, y+1, 0))
                new_pos.append((x+1, y, 1))
            if board[y][x-1] == 0 and board[y+1][x-1] == 0:
                new_pos.append((x-1, y, 0))
                new_pos.append((x-1, y+1, 0))
                new_pos.append((x-1, y, 1))

        for pos in new_pos:
            if pos not in visited:
                visited[pos] = True
                queue.append(pos+(time+1,))
    return -1

if __name__ == "__main__":
    print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))