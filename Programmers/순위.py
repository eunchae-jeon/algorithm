def solution(n, results):
    answer = 0
    table = [[0] * n for _ in range(n)]
    for r in results:
        table[r[0]-1][r[1]-1] = 1
        table[r[1]-1][r[0]-1] = -1
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j == i or k == i or j == k or table[j][k] != 0: continue
                if table[i][k] + table[j][i] > 1:
                    table[j][k] = 1
                elif table[i][k] + table[j][i] < -1:
                    table[j][k] = -1
    for line in table:
        if line.count(0) == 1:
            answer += 1
    print(answer)
    return answer


if __name__ == "__main__":
    solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])