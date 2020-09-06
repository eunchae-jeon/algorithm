def solution(n, times):
    maxtime = max(times)*n/len(times)
    mintime = 0
    answer = maxtime
    while maxtime >= mintime:
        mid = (maxtime + mintime)//2
        sumn = 0
        for t in times:
            sumn += mid // t
        if sumn >= n:
            if answer > mid:
                answer = mid
            maxtime = mid-1
        else:
            mintime = mid+1

    return answer
