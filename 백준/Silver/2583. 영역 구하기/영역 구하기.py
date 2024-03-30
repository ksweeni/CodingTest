import sys
sys.setrecursionlimit(10000)

m,n,k= map(int, input().split())
board = [[0] * n for i in range(m)]
empty = []
for i in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  for y in range(y1,y2):
    for x in range (x1,x2):
      board[y][x] = 1

D = [(0,1),(0,-1),(1,0),(-1,0)]

def dfs(x,y,count):
  board[y][x] =1
  for dx, dy in D:
    newX = x+dx
    newY = y+dy
    if(0 <= newX < n) and (0 <= newY < m) and board[newY][newX]==0:
      count = dfs(newX, newY, count+1)
  return count

for y in range(m):
  for x in range(n):
    if board[y][x]==0:
      empty.append(dfs(x,y,1))
      
print(len(empty))
print(*sorted(empty))