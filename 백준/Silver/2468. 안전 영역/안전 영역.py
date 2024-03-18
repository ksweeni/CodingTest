from collections import deque

n = int(input())
board = []
maxnum = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
  board.append(list(map(int, input().split())))
  for j in range(n):
    if board[i][j] > maxnum:
      maxnum = board[i][j]

def bfs(x,y,val,visited):
  que = deque()
  que.append((x,y))
  visited[x][y] = True

  while que:
    px, py = que.popleft()
    for i in range(4):
      cx = px+dx[i]
      cy = py+dy[i]
      if 0<=cx<n and 0<=cy<n and visited[cx][cy]==False and board[cx][cy] > val:
        visited[cx][cy]=True
        que.append((cx,cy))


answer = 0
for i in range(maxnum):
  visited = [[False] * n for i in range(n)]
  cnt = 0
  
  for j in range(n):
    for k in range(n):
      if board[j][k] > i and visited[j][k]==False:
        bfs(j,k,i,visited)
        cnt+=1
        
  if answer < cnt:
    answer=cnt
    
print(answer)