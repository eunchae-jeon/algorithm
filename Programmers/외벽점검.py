from itertools import permutations
def solution(n, weak, dist):
    if len(weak) == 0:
        return 0
    max_dist = 0
    start_i = 0
    prev = weak[-1] - n
    for i, w in enumerate(weak):
        if w - prev > max_dist:
            max_dist = w - prev
            start_i = i
        prev = w
    weak = weak[start_i:] + [w + n for w in weak[:start_i]]#가장 큰 간격 제거후 직선화
    dist.sort(reverse=True)
    for answer in range(1, len(dist)+1):
        for ds in permutations(dist[:answer], answer):
            cur_i = 0
            for d in ds:
                for i in range(cur_i, len(weak)):
                    if weak[cur_i] + d < weak[i]:
                        cur_i = i
                        break
                else:
                    return answer

    return -1

if __name__ == "__main__":
    print(solution(12,	[1, 5, 6, 10],	[1, 2, 3, 4]))
    # print(solution(12,  [1, 3, 4, 9, 10],	[3, 5, 7]))
    # print(solution(50,  [1],	[3]))