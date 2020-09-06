from collections import deque

def solution(numbers):
    # not_primes = set()
    all_num = set()
    stack = deque([("", numbers)])

    while len(stack) > 0:
        num = stack.pop()
        if num[1] != "":
            for i in range(len(num[1])):
                stack.append((num[0]+num[1][i], num[1][:i]+num[1][i+1:]))
                if num[0] != "":
                    all_num.add(int(num[0]))
        else:
            all_num.add(int(num[0]))
    all_num = all_num - {0, 1}
    answer = []
    for num in all_num:
        div = 2
        while div**2 <= num:
            # if div not in not_primes:
            if num % div == 0:
                break
            div += 1   
        else:
            answer.append(num)
    print(answer)
    return len(answer)


print(solution("1234"))
