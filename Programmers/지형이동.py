from collections import deque
import heapq
def solution(land, height):
    N = len(land)
    visited = [[False] * N for _ in range(N)]
    costs = []
    answer = 0

    stack = deque([(0, 0)])
    count = 0
    visited[0][0] = True
    while True:
        while stack:
            pos = stack.pop()
            
            # if pos in costs:
            #     del costs[pos]
            count += 1
            next_pos = []
            if pos[0] > 0:
                next_pos.append((pos[0]-1, pos[1]))
            if pos[0] < N-1:
                next_pos.append((pos[0]+1, pos[1]))
            if pos[1] > 0:
                next_pos.append((pos[0], pos[1]-1))
            if pos[1] < N-1:
                next_pos.append((pos[0], pos[1]+1))
            for n in next_pos:
                if visited[n[0]][n[1]] == True:
                    continue
                diff = abs(land[pos[0]][pos[1]] - land[n[0]][n[1]])
                if diff > height:
                    heapq.heappush(costs, (diff, n))
                else:
                    stack.append(n)
                    visited[n[0]][n[1]] = True
            # print("stack" ,stack)       
            # print("costs" ,costs)
            # print("count", count)
                
        
        if count < N*N:
            # start = (-1, -1)
            # mini = 10000
            # for k in costs.keys():
            #     if costs[k] < mini:
            #         start = k
            #         mini = costs[k]
            # answer += mini
            # stack.append(start)
            while True:
                start = heapq.heappop(costs)
                if visited[start[1][0]][start[1][1]] == False:
                    break
            answer += start[0]
            stack.append(start[1])  
            visited[start[1][0]][start[1][1]] = True
        else:
            break
                
    return answer

if __name__ == "__main__":

    print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))