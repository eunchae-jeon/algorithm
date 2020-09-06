def solution(N, number):
    if number == N:
        return 1

    possible = [{0},{N}]
    num_of_N = 2

    while True:
        if num_of_N > 8:
            return -1

        sub_possible = {int(str(N) * num_of_N)}
        for i in range(1, num_of_N//2 + 1):
            for x in possible[i]:
                for y in possible[num_of_N - i]:
                    sub_possible.add(x+y)
                    sub_possible.add(x*y)
                    sub_possible.add(x-y)
                    sub_possible.add(y-x)
                    if y != 0:
                        sub_possible.add(x//y)
                    if x != 0:
                        sub_possible.add(y//x)
            
        if number in sub_possible:
            return num_of_N
        
        possible.append(sub_possible)
        num_of_N += 1

    return -1