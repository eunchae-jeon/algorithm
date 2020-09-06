def solution(user_id, banned_id):
    visited = [0] * len(user_id)
    ans_set = set([])
    dfs(user_id, banned_id, 0, visited, ans_set)
    return len(ans_set)

def comp(user, ban):
    if len(user) != len(ban):
        return False
    for u, b in zip(user, ban):
        if b == "*" or u == b:
            continue
        else:
            return False
    return True

def visit2int(visited):
    ret = 0
    for v in visited:
        ret *= 2
        ret += v
    return ret

def dfs(user_id, banned_id, n, visited, ans_set):
    if n == len(banned_id):
        ans_set.add(visit2int(visited))
        return

    for i, user in enumerate(user_id):
        if comp(user, banned_id[n]) == True and visited[i] == 0:
            v = visited[:]
            v[i] = 1
            dfs(user_id, banned_id, n+1, v, ans_set)

if __name__ == "__main__":
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "abc1**"]))