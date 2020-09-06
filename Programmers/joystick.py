def solution(name):
    answer = 0
    answer += cal_leng(name)
    for n in name:
        answer += char_to_num(n)
    return answer

def char_to_num(char):
    ret = ord(char)-65
    if ret > 12:
        ret = 26 - ret
    return ret

def cal_leng(name):
    max_conti_a = 0
    conti_a_start = -1
    temp = 0
    leng = 0
    for i, n in enumerate(name):
        if n == 'A':
            temp += 1
        else:
            if temp > max_conti_a:
                max_conti_a = temp
                conti_a_start = i - temp
            temp = 0
    if temp != 0:
        leng = len(name) - 1 - temp
    else:
        if conti_a_start == -1 :
            conti_a_start = 1
        elif conti_a_start == 0:
            conti_a_start = 2
        leng = min(len(name) - 1, conti_a_start - 1 + len(name) - max_conti_a - 1)
    return leng




