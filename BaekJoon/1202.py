import sys
import heapq
In = sys.stdin.readline
def solution():
    n, k = map(int, In().split())
    jewelry = [list(map(int, In().split())) for _ in range(n)]
    cap = [int(In()) for _ in range(k)]
    ans = 0
    jewelry.sort(key=lambda v: v[0])
    cap.sort()
    pq = []
    j = 0
    for c in cap:
        while j < len(jewelry):
            if c >= jewelry[j][0]:
                heapq.heappush(pq, -jewelry[j][1])
            else:
                break
            j += 1
        if pq:
            ans -= heapq.heappop(pq)
    return ans

print(solution())
