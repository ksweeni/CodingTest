def solution(n, computers):
    def dfs(node):
            visited[node] = True # 방문 표시
            for i in range(n):
                if not visited[i] and computers[node][i]: # 방문안한, 인접노드
                    dfs(i)
                
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1 # 뭉탱이의 개수
    return answer