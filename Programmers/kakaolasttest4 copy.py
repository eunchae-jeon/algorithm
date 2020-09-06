def solution(k, room_number):
    answer = [0 for _ in range(len(room_number))]
    next_room = [i for i in range(k+1)]
    for i, r in enumerate(room_number):
        idxs = [r]
        idx = r
        while next_room[idx] != idx:
            idx = next_room[idx]
            idxs.append(idx)
        answer[i] = idx
        idx += 1
        while len(next_room) > idx and next_room[idx] != idx:
            idxs.append(idx)
            idx += 1
        idxs.append(idx)

        for index in idxs:
            next_room[index] = idx
        
        # next_room[r] = idx
        # next_room[answer[i]]= idx
        # print(next_room)

    return answer

print(solution(10,[1,3,4,1,3,1]))