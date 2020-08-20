n = int(input())
arr=list()
count=0
for i in range(n):
  p,v,t = map(int,input().split())
  arr.append([p,v,t])

for i in arr:
  sure=0
  for j in i:
    if j ==1:
      sure +=1
    else:
      continue
  if sure>=2:
    count+=1

print(count)



'''
3
1 1 0
1 1 1
1 0 0
'''