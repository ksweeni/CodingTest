n = int(input())
wine = [0] * 10001
for i in range(1, n + 1):
  wine[i] = int(input()) # 포도주의 양

# dp
dp = [0] * 10001 
dp[1] = wine[1]  
dp[2] = wine[1] + wine[2] 

for i in range(3, n + 1): 
		# 참고
    # 현재 포도주를 마시지 않았을 경우, 현재 포도주와 이전 포도주를 마셨을 경우, 마시지 않았을 경우를 비교
    dp[i] = max(dp[i - 1], wine[i] + wine[i - 1] + dp[i - 3], wine[i] + dp[i - 2])

print(max(dp))