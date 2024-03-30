from collections import deque
import copy
d = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs():
    queue = deque()
    copied = copy.deepcopy(lab_map)
    for i in range(n):
        for k in range(m):
            if copied[i][k] == 2:
                queue.append((i,k))

    while queue:
        ii,jj = queue.popleft()

        for i in range(4):
            dr = ii+d[i][0]
            dc = jj+d[i][1]

            if (0<=dr<n) and (0<=dc<m):
                if copied[dr][dc] == 0:
                    copied[dr][dc] =2
                    queue.append((dr,dc))

    global res
    count = 0
    for i in range(n):
        for k in range(m):
            if copied[i][k] == 0:
                count +=1

    res = max(res, count)

def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for k in range(m):
            if lab_map[i][k] == 0:
                lab_map[i][k] = 1
                make_wall(count+1)
                lab_map[i][k] = 0
n, m = map(int,input().split())
lab_map = [list(map(int,input().split())) for _ in range(n)]
res = 0
make_wall(0)
print(res)