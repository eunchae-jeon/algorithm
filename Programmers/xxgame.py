def solution(land, P, Q):
    d = {}
    for x in land:
        for y in x:
            if y in d:
                d[y] += 1
            else:
                d[y] = 1
    heights = d.keys()
    maxh = max(heights)
    minh = min(heights)
    for i in range(minh, maxh):
        if i not in d:
            d[i] = 0

    plist = [d[i] for i in range(minh, maxh+1)]
    qlist = [d[i] for i in range(minh, maxh+1)]
    
    plocal = 0
    qlocal = 0
    pprev = 0
    qprev = 0
    for i in range(len(plist)):
        temp = plist[i]
        plist[i] = plocal + pprev
        plocal += temp
        pprev = plist[i]

        temp = qlist[len(qlist)-1 - i]
        qlist[len(qlist)-1 - i] = qlocal + qprev
        qlocal += temp
        qprev = qlist[len(qlist)-1 - i]

    # print(plist)
    # print(qlist)
    costs = [P*plist[i]+Q*qlist[i] for i in range(len(plist))]
    answer = min(costs)
    return answer



print(solution([[1, 2], [2, 3]], 3, 2))
print(solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3))