import heapq

def solution(scoville, K):
    q = []
    for s in scoville:
        heapq.heappush(q, s)
    count = 0
    while True:
        try:
            min_scoville = heapq.heappop(q)
        except:
            return -1

        if min_scoville >= K:
            return count

        else:
            try:
                min2_scoville = heapq.heappop(q)
            except:
                return -1
            
            heapq.heappush(q, min_scoville+min2_scoville*2)
            count += 1

        # print(q, count)

# solution([1, 2, 3, 9, 10, 12], 7)