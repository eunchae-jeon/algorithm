import collections
def solution(people, limit):
    people.sort()
    deq = collections.deque(people)
    boat = 0
    while len(deq) > 0:
        if len(deq) > 1 and limit - deq[-1] >= deq[0]:
            deq.popleft()
        deq.pop()
        boat += 1
    return boat

print(solution([50, 50, 70, 80], 100))
