def solution(n, build_frame):
    answer = [[]]
    build_dict = {}
    matrix = [[0] * (n+1) for _ in range(n+1)]
    matrix[0] = [1]*(n+1)

    for b in build_frame:
        x, y, t, c = b
        if c == 1:
            if t == 0:
                if matrix[y][x] >= 1:
                    matrix[y+1][x] += 2
                    build_dict[(x,y,t)] = True
            elif t == 1:
                if matrix[y][x] + matrix[y][x+1] >= 2:
                    matrix[y][x] +=1
                    matrix[y][x+1] += 1
                    build_dict[(x,y,t)] = True
        elif c == 0:
            if t == 0:
                if (x, y+1, 1) in build_dict and matrix[y+1][x] + matrix[y+1][x+1] - 4 < 2:
                    continue
                if (x-1, y+1, 1) in build_dict and matrix[y+1][x] + matrix[y+1][x-1] - 4 < 2:
                    continue
                if (x, y+1, 0) in build_dict and matrix[y+1][x] - 2 < 1:
                    continue
                matrix[y+1][x] -= 2
                del build_dict[(x,y,t)]
            if t == 1:
                if (x-1, y, 1) in build_dict and matrix[y][x] + matrix[y][x-1] - 3 < 2:
                    continue
                if (x+1, y, 1) in build_dict and matrix[y][x+1] + matrix[y][x+2] - 3 < 2:
                    continue
                if (x, y, 0) in build_dict and matrix[y][x] - 1 < 1:
                    continue
                if (x+1, y, 0) in build_dict and matrix[y][x+1] - 1 < 1:
                    continue
                matrix[y][x] -= 1
                matrix[y][x+1] -= 1
                del build_dict[(x,y,t)]
    return  list(map(list, sorted(build_dict.keys())))

if __name__ == "__main__":
    # print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
    print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))