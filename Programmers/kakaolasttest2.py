def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s = [list(map(int, st.split(","))) for st in s]
    s.sort(key= lambda l: len(l))
    for st in s:
        for num in st:
            if num not in answer:
                answer.append(num)
                break


    return answer

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))