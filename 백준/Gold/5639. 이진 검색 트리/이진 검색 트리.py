import sys
sys.setrecursionlimit(10**6)
tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

def getTree(first,end):
    if first > end:
        return
    mid = end+1   # 참고 : 루트보다 큰 값이 존재하지 않을 경우를 대비   
    for i in range(first+1,end+1):
        if tree[first] < tree[i]:
            mid = i
            break

    getTree(first+1, mid-1)
    getTree(mid, end)
    print(tree[first])

getTree(0,len(tree)-1)