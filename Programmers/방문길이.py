def solution(dirs):
    answer = 0
    dir_dict = {"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)}
    dic = {}
    x, y = 0, 0
    for d in dirs:
        if -5 <= x+dir_dict[d][0] <= 5 and -5 <= y+dir_dict[d][1] <= 5:
            ox, oy = x, y
            x += dir_dict[d][0]
            y += dir_dict[d][1]
            if d == "L":
                ox = x
                d = "R"
            if d == "D":
                oy = y
                d = "U"
            if (ox, oy, d) not in dic:
                answer += 1
                dic[(ox, oy, d)] = True
    return answer

if __name__ == "__main__":
    print(solution("ULURRDLLU"))