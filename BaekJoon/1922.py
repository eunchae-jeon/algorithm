import sys
In = sys.stdin.readline

def solution():
    n = int(In())
    m = int(In())
    cycle = [i for i in range(n+1)]
    costs = [list(map(int, In().split())) for _ in range(m)]
    costs = sorted(costs, key = lambda cost : cost[2])
    answer = 0
    for cost in costs:
        a = find_group(cycle, cost[0])
        b = find_group(cycle, cost[1])
        if a == b: continue
        if a > b:
            cycle[a] = b
        else:
            cycle[b] = cycle[a]
        answer += cost[2]
    return answer

def find_group(cycle, v):
    if cycle[v] == v: return v
    return find_group(cycle, cycle[v])

if __name__ == "__main__":
    print(solution())