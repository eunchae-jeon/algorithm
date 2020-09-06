import heapq

def solution(stock, dates, supplies, k):
    q = []
    count = 0
    for i, date in enumerate(dates):
        while stock < date:
            try:
                stock -= heapq.heappop(q)
                count += 1
            except:
                return -1
        heapq.heappush(q, -supplies[i])
    else:
        while stock < k:
            try:
                stock -= heapq.heappop(q)
                count += 1
            except:
                return -1
    return count

# solution(4,	[4,10,15],	[20,5,10],	30)