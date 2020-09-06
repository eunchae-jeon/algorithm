def solution(gems):
    answer = [0,len(gems)]
    dic = {}
    kind = len(set(gems))
    flag = False
    mini = 0
    min_gem = gems[0]
    for i, gem in enumerate(gems):
        dic[gem] = i
        if min_gem == gem:
            mini = min(dic.values())
            min_gem = gems[mini]
        if flag == False and len(dic) == kind:
            flag = True
        if flag == True:
            mn, mx = mini, i
            if answer[1]-answer[0] > mx - mn:
                answer = [mn+1, mx+1]
    return answer

    

if __name__ == "__main__":
    print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))

    