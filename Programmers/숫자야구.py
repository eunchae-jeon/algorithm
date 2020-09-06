from itertools import permutations
from functools import reduce

def solution(baseball):
    no_answer = set()
    answer = [i for i in range(1, 10)]
    answer = list(permutations(answer, 3))
    answer = list(map(lambda a : reduce(lambda x, y: x + str(y), a, ""), answer))
    for data in baseball:
        num1 = str(data[0])
        print(no_answer)
        for num0 in answer:
            s = 0
            b = 0   
            if num0 in no_answer:
                continue
            for i in range(0, 3):
                for j in range(0, 3):
                    if num0[i] == num1[j]:
                        if i == j:
                            s += 1
                        else:
                            b += 1
            if s != data[1] or b != data[2]:
                no_answer.add(num0)
            

    return 9*8*7-len(no_answer)





if __name__ == "__main__":
    print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))