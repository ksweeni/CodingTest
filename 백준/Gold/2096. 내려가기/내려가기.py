n = int(input()) 
a, b, c = map(int, input().split())
maxdp = [a,b,c]
mindp = [a,b,c]

for i in range(1,n):
  x,y,z= map(int, input().split())
  for j in range(3):
    if j == 0:
      max1 = max(maxdp[0], maxdp[1])+x
      min1 = min(mindp[0], mindp[1])+x
    if j == 1:
      max2 = max(maxdp[0], maxdp[1], maxdp[2])+y
      min2 = min(mindp[0], mindp[1], mindp[2])+y
    if j == 2:
      max3 = max(maxdp[1], maxdp[2])+z
      min3 = min(mindp[1], mindp[2])+z
  maxdp = [max1, max2, max3]
  mindp = [min1, min2, min3]
print(max(maxdp), min(mindp))