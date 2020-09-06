def solution(snapshots, transactions):
    answer = []
    done = {}
    accounts = {}
    for data in snapshots:
        accounts[data[0]] = int(data[1])
    for data in transactions:
        if data[0] in done:
            continue
        done[data[0]] = 1
        if data[1] == "SAVE":
            try:
                accounts[data[2]] += int(data[3])
            except:
                accounts[data[2]] = int(data[3])
        elif data[1] == "WITHDRAW":
            if data[2] in accounts  and accounts[data[2]] >= int(data[3]):
                accounts[data[2]] -= int(data[3])

    for key in accounts.keys():
        answer.append([key, str(accounts[key])])
    answer.sort()
    return answer

print(solution([
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"],
  ["ACCOUNT10", "150"]
],
[
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]
))