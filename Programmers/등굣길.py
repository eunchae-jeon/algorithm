def solution(m, n, puddles):
    routes = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles:
                routes[i][j] = 0
            elif i == 0 and j == 0:
                routes[i][j] = 1
            elif i == 0:
                routes[i][j] = routes[i][j-1]
            elif j == 0:
                routes[i][j] = routes[i-1][j]
            else:
                routes[i][j] = routes[i-1][j] + routes[i][j-1]
    return routes[i][j]%1000000007



print(solution(4, 3, [[2, 2]]))