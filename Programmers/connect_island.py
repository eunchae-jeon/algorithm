def solution(n, costs):
    total = 0
    cycle_table = [n for n in range(n)]
    costs = sorted(costs, key=lambda c: c[2])
    for cost in costs:
        if cycle_table[cost[0]] != cycle_table[cost[1]]:
            temp = cycle_table[cost[1]]
            for i in range(len(cycle_table)):
                if cycle_table[i] == temp:
                    cycle_table[i] = cycle_table[cost[0]]
            total += cost[2]

    return total

print(solution(4,[[0,1,1],[0,2,2],[2,3,1]]))