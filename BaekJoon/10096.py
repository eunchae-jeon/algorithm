import sys
In = sys.stdin.readline

def solution():
    n = int(In())
    u = In().rstrip()
    if n % 2 == 0: return 'NOT POSSIBLE' #길이가 짝수면 불가능
    s_length = n//2
    for char in u:
        if u[0] != char: break
    else:
        return u[:s_length] #모두 같은 문자일 땐 유일한 S
    if u[:s_length] == u[s_length:-1] and u[1:s_length+1] == u[s_length+1:]:
        return 'NOT UNIQUE' #정답이 여러개이려면 맨 앞을 제외하고 반씩 똑같거나 맨 뒤를 제외하고 반씩 똑같아야함

    right = s_length+1 #왼쪽에 삽입했다고 가정 (가운데 포함)
    for i in range(s_length):
        if u[i] != u[right+i]: #왼쪽 값이 불순물
            if u[i+1:s_length+1] == u[right+i:]:#불순물 제외 마지막까지 같으면
                return u[right:]
            else: break #오른쪽 검사
    else: #가운데가 불순물인 경우
        return u[right:]
    right = s_length #오른쪽에 삽입했다고 가정
    for i in range(s_length):
        if u[i] != u[right+i]: #오른쪽 값이 불순물
            if u[i:s_length] == u[right+i+1:]:#불순물 제외 마지막까지 같으면
                return u[:s_length]
            else: return 'NOT POSSIBLE'
    else:#오른쪽 끝이 불순물인 경우
        return u[:s_length]

if __name__ == "__main__":
    print(solution())