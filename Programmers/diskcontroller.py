import heapq

def solution(jobs):
    jobs.sort()
    q = []
    endsum = 0
    endtime = 0
    curtime = 0
    i = 0
    while True:
        if i >= len(jobs):
                break
        if jobs[i][0] <= curtime:
            
            heapq.heappush(q, jobs[i][1])
            i += 1
            continue

        else:
            try:
                endtime = curtime + heapq.heappop(q)
                endsum += endtime
                curtime = endtime
                print("endtime {}".format(endtime))
            except:
                curtime = jobs[i][0]
                print("ex")
            
        print(q)
    while True:
        try:
            endtime = curtime + heapq.heappop(q)
            endsum += endtime
            curtime = endtime
            print("endtime {}".format(endtime))
        except:
            break
    answer = (endsum - sum([j[0] for j in jobs])) // len(jobs)
    return answer

# print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))
# print(solution([[0, 1], [3, 1]]))
print(solution([[0, 3], [1, 9], [2, 6]]))