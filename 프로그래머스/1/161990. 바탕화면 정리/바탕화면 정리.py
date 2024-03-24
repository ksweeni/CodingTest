from collections import *
def solution(wallpaper):

    que = deque()
    for widx, wall in enumerate(wallpaper):
        for idx, w in enumerate(wall):
            if w=='#':
                que.append((widx, idx))
                
    maxX = 0
    maxY = 0
    minX = 1001
    minY = 1001
    while que:
        x, y = que.popleft()
        maxX = max(x, maxX)
        maxY = max(y,maxY)
        minX = min(x, minX)
        minY = min(y, minY)
    print(maxX,maxY)
    print(minX,minY)
    return [minX,minY,maxX+1,maxY+1 ]
    
    

