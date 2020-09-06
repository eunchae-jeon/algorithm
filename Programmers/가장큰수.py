from functools import cmp_to_key

def solution(numbers):
    answer = [str(num) for num in numbers]
    answer = sorted(answer, key=cmp_to_key(cmp_items))
    answer = ''.join(answer)
    for i, a in enumerate(answer):
        if a == '0':
            continue
        else:
            break
    answer = answer[i:]
    return answer

def cmp_items(a, b):
    if a+b < b+a:
        return 1
    elif a+b > b+a:
        return -1
    else:
        return 0


# 0000예외
   # for i in range(max(len(a), len(b))):
    #     if a[i % len(a)] < b[i % len(b)]:
    #         return 1
    #     elif a[i % len(a)] > b[i % len(b)]:
    #         return -1
    #     else:
    #         return 0


print(solution(	[1, 10, 20, 30]))