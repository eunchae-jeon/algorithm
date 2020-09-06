import collections
def solution(board, moves):
    answer = 0
    n = len(board)
    idxs = [-1 for _ in range(n)]
    stack = collections.deque()
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 and idxs[j] == -1:
                idxs[j] = i
    
    for move in moves:
        move -= 1
        if idxs[move] == -1:
            continue
        else:
            if len(stack) > 0 and stack[-1] == board[idxs[move]][move]:
                stack.pop()
                answer += 2
            else:
                stack.append(board[idxs[move]][move])
            idxs[move] += 1
            if idxs[move] == n:
                idxs[move] = -1

    return answer