# from collections import deque
def solution(n):
    sum_dic = {}
    sub_dic = {}
    answer = [0]
    visit = [False] * n

    def dfs(x, y):
        if y+1 == n:
            answer[0] += 1
        sum_dic[x+y] = True
        sub_dic[x-y] = True
        for nx, v in enumerate(visit):
            if v == False:
                if sum_dic.get(nx+y+1, False) == False and sub_dic.get(nx-y-1, False) == False:
                    visit[nx] = True
                    dfs(nx, y+1)
        sum_dic[x+y] = False
        sub_dic[x-y] = False
        visit[x] = False

    for j in range(n):
        visit[j] = True
        dfs(j, 0)
        visit[j] = False

    return answer[0]

if __name__ == "__main__":
    print(solution(10))