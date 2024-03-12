def solution(numbers, target):
    answer = 0
    end = len(numbers)
    def dfs(idx, total):
        if idx == end:
            if total == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, total+numbers[idx])
            dfs(idx+1, total-numbers[idx])
    dfs(0,0)
    return answer