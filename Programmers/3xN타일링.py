def solution(n):
    if n % 2 == 1 or n == 0:
        return 0

    n //= 2
    unlinked, unlinked_prev, linked = 3, 1, 0
    for _ in range(1, n):
        unlinked, linked = (unlinked + linked) * 3, unlinked_prev * 2 + linked
        unlinked_prev = unlinked//3
        # print(unlinked, linked, unlinked_prev)
    return unlinked + linked
print(solution(5000))