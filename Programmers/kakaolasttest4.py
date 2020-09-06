import bisect
import collections
def solution(k, room_number):
    answer = [0 for _ in range(len(room_number))]
    remain_rooms = collections.deque()
    for i in range(k):
        remain_rooms.append(i+1)
    for i, r in enumerate(room_number):
        idx = bisect.bisect_left(remain_rooms, r, lo=0, hi=len(remain_rooms))
        answer[i] = remain_rooms[idx]
        del remain_rooms[idx] 

    return answer