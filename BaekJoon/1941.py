import itertools
import collections
import sys
In = sys.stdin.readline

def solution():
    answer = 0
    students = [In().rstrip() for _ in range(5)]
    positions = [(i, j) for i in range(5) for j in range(5)]
    for combination in itertools.combinations(positions, 7):
        if isAdjacent(combination):
            group = [students[pos[0]][pos[1]] for pos in combination]
            if group.count('S') > 3:
                answer += 1
    return answer

def isAdjacent(positions):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    queue = collections.deque([positions[0]])
    visited = {pos: False for pos in positions}
    visited[positions[0]] = True
    count = 0
    while queue:
        cur = queue.popleft()
        count += 1
        if count == 7:
            return True
        for i in range(4):
            y = cur[0] + dy[i]
            x = cur[1] + dx[i] 
            if (y, x) in visited and visited[(y, x)] == False:
                visited[(y, x)] = True
                queue.append((y, x))
    return False

if __name__ == "__main__":
    print(solution())