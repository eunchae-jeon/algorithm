import sys
from collections import deque
In = sys.stdin.readline
def solution():
    N, M, K = map(int, In().split())
    A = [list(map(int, In().split())) for _ in range(N)]
    alltrees = [[[] for _ in range(N)] for _ in range(N)]
    # tree_dict = [deque() for i in range(N) for j in range(N)]
    ground = [[5] * N for _ in range(N)]
    init_tree = [tuple(map(int, In().split())) for _ in range(M)]

    init_tree = sorted(init_tree, key=lambda x: x[2])

    for itree in init_tree:
        x, y, z = itree
        # tree_dict[(x-1, y-1)].append(z)
        alltrees[x-1][y-1].append(z)
    
    for _ in range(K):
        for i in range(N):
            for j in range(N):
                trees = alltrees[i][j]
                # trees.sort()
                s_trees = []
                for k, tree in enumerate(trees):
                    if ground[i][j] >= tree:
                        ground[i][j] -= tree
                        s_trees.append(tree+1)
                    else:
                        ground[i][j] += sum(d//2 for d in trees[k:])
                        break
                alltrees[i][j] = s_trees
                ground[i][j] += A[i][j]
        
        for i in range(N):
            for j in range(N):
                trees = alltrees[i][j]
                count = 0
                for tree in trees:
                    if tree%5 == 0: count += 1
                if count == 0: continue
                for x in (-1, 0, 1):
                    for y in (-1, 0, 1):
                        ni, nj = i+x, j+y
                        if ni < 0 or ni >= N or nj < 0 or nj >= N or (x==y and x==0): continue
                        alltrees[ni][nj] = [1]*count + alltrees[ni][nj]

    answer = 0
    for i in range(N):
        for j in range(N):
            answer += len(alltrees[i][j])
        
    return answer

print(solution())
    

    