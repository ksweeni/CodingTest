import sys
input = sys.stdin.readline
n = int(input())  
number = list(map(int, input().split()))  
m = int(input())  
start, end = 0, max(number)

while start <= end:  # 이분탐색
    mid = (start + end) // 2  
    total = 0
  
    for i in number:
      total += min(i, mid)
       
    if total <= m:  
        start = mid + 1
    else:  
        end = mid - 1
print(end)