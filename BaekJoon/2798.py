import sys
from itertools import combinations
In = sys.stdin.readline

def solution():
    answer = 0
    N, target = map(int, In().split())
    cards = list(map(int, In().split()))
    for c in combinations(cards, 3):
        s = sum(c)
        if s <= target and s > answer:
            answer = s
    return answer

if __name__ == "__main__":
    print(solution())