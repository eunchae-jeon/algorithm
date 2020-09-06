def solution(s):
    answer = 0
    for i in range(len(s)):
        leng = 0
        for j in range(0, len(s)):
            if i-j < 0 or i+j >= len(s): break
            if s[i-j] == s[i+j]:
                leng = j*2+1
                continue
            break
        if leng > answer:
            answer = leng
        for j in range(0, len(s)):
            if i-j < 0 or i+1+j >= len(s): break
            if s[i-j] == s[i+j+1]:
                leng = j*2+2
                continue
            break
        if leng > answer:
            answer = leng
    return answer

print(solution("aa"))