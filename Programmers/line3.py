def solution(road, n):
    num_road = string_2_num(road)
    if len(num_road) < n+1:
        return sum(num_road)+len(num_road)-1
    local = sum(num_road[:n+1])
    answer = local
    for i in range(len(num_road)-n-1):
        local += (num_road[i+n+1] - num_road[i])
        if num_road[i] < num_road[i+n+1]:
            answer = local
    return answer + n

def string_2_num(road):
    num = []
    temp = 0
    for r in road:
        if r == '0':
            num.append(temp)
            temp = 0
        elif r == '1':
            temp += 1
    num.append(temp)
    return num

print(solution("111011110011111011111100011111", 3))
