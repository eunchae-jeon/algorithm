# from collections import deque
def solution(tickets):
    tickets.sort()
    N = len(tickets) + 1
    answer = ["ICN"]

    def dfs(cur, ts, an):
        if len(an) == N:
            return an

        for i in range(len(ts)):
            if ts[i][0] == cur:
                a = an[:]
                a.append(ts[i][1])
                temp = dfs(ts[i][1], ts[:i]+ts[i+1:], a)
                if temp != None:
                    return temp

        
    return dfs("ICN", tickets, answer)
    



if __name__ == "__main__":
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"], ["SFO", "AAA"], ["AAA", "ICN"]]))