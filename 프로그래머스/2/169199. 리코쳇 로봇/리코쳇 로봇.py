from collections import *
def solution(board):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    que = deque() # 덱 선언
    fx = len(board)
    fy = len(board[0])
    distance = [[987654321 for _ in range(fy)] for _ in range(fx)]
 
    # R 위치 찾기
    for i in range(fx):
        for j in range(fy):
            if board[i][j]=='R':
                que.append((i,j,0))
                distance[i][j] = 0
        if que:
            break
 
    
    # BFS 돌기
    while que:
        x,y,z = que.popleft()
        if board[x][y]=='G':
            return z
        for i in range(4):
            cx = x
            cy = y
            
            while 0<=cx+dx[i]<fx and 0<=cy+dy[i]<fy and board[cx+dx[i]][cy+dy[i]]!='D':
                cx+=dx[i]
                cy+=dy[i]
                
            # <참고> 이전에 해당 위치에 도달한 적이 없거나, 이전에 도달한 경우보다 적은 이동 횟수로 도달 가능한 경우
            if distance[cx][cy] > z+1:
                distance[cx][cy]=z+1
                que.append((cx,cy,z+1))
    return -1