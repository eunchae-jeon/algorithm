def solution(answer_sheet, sheets):
    answer = -1

    for i in range(len(sheets)):
        for j in range(i+1, len(sheets)):
            num = 0
            leng = 0
            longest = 0
            prev = False
            for k in range(len(answer_sheet)):
                if sheets[i][k] == sheets[j][k] and sheets[i][k] != answer_sheet[k]:
                    num += 1
                    if prev == True:
                        leng += 1
                    else:
                        leng = 1
                    prev = True
                else:
                    prev = False
                    if leng > longest:
                        longest = leng
                    leng = 0
            if leng > longest:
                longest = leng
            p =  num + longest**2
            if p > answer:
                answer = p

    return answer

print(solution("4132315142", ["3241523133","4121314445","3243523133","4433325251","2412313253"]))