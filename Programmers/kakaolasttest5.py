import heapq
def solution(stones, k):
    local_max = []
    to_pop = []
    
    for j in range(k):
        heapq.heappush(local_max, -stones[j])
    answer = -local_max[0]
    for i in range(len(stones)-k):
        
        heapq.heappush(to_pop, -stones[i])
        heapq.heappush(local_max, -stones[i+k])
        # print(local_max)
        # print(to_pop)
        # print("")
        while len(to_pop) > 0 and to_pop[0] == local_max[0]:
            heapq.heappop(to_pop)
            heapq.heappop(local_max)
        # print(local_max)
        # print(to_pop)
        # print("---")
        if -local_max[0] < answer:
            answer = -local_max[0]
        
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))