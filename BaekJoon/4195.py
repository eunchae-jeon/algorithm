import sys
In = sys.stdin.readline

def solution():
    N = int(In())
    for _ in range(N):
        F = int(In())
        dic = {}
        len_dic = {}
        for _ in range(F):
            person0, person1 = In().split()
            parent0 = find_parent(dic, person0)
            parent1 = find_parent(dic, person1)
            if parent0 not in len_dic:
                len_dic[parent0] = 1
            if parent1 not in len_dic:
                len_dic[parent1] = 1
            if parent0 == parent1:
                print(len_dic[parent0])
            elif len_dic[parent0] > len_dic[parent1]:
                len_dic[parent0] += len_dic[parent1]
                dic[parent1] = parent0
                print(len_dic[parent0])

            else:
                len_dic[parent1] += len_dic[parent0]
                dic[parent0] = parent1
                print(len_dic[parent1])
    return

def find_parent(dic, child):
    while dic.get(child, child) != child:
        child = dic[child]
    return child


if __name__ == "__main__":
    solution()