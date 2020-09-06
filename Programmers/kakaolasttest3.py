import collections

def solution(user_id, banned_id):
    answer = 0
    selected = [0 for _ in range(len(user_id))]

    answer = trav(selected, 0, user_id, banned_id)


    return answer

def trav(remain_user, ban_idx, user_id, banned_id):
    if ban_idx == len(banned_id):
        # print(remain_user)
        if mask(remain_user) not in d:
            d[mask(remain_user)] = 1
            return 1
        else:
            return 0
    ret = 0
    for i in range(len(remain_user)):
        if remain_user[i] == 0 and comp(user_id[i], banned_id[ban_idx]):
            temp = remain_user[:]
            temp[i] = 1
            ret += trav(temp, ban_idx+1, user_id, banned_id)
    return ret

def comp(user, ban):
    if len(user) != len(ban):
        return False
    
    for i in range(len(user)):
        if ban[i] == "*" or ban[i] == user[i]:
            continue
        else:
            return False
    else:
        return True

def mask(remain_user):
    ret = 0
    for i, r in enumerate(remain_user):
        if r == 1:
            ret += 2**i

    return ret

d = {}

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))