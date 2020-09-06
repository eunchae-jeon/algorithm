def solution(budgets, M):

    remain = len(budgets)

    budgets.sort()
    for budget in budgets:
        if remain * budget > M:
            return M // remain

        remain -= 1
        M -= budget


    return budget