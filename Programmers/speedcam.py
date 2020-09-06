import heapq

def solution(routes):
    routes.sort()
    count = 0
    q = []
    for route in routes:
        cur = route[0]
        if len(q) > 0 and cur > q[0]:
            count += 1
            q = []
        heapq.heappush(q, route[1])
        print(q)

    return count+1

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))