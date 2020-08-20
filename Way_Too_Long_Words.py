n = int(input())
arr =list()
for i in range(n):
  word = input()
  arr.append(word)

for ele in arr:
  if len(ele)>10:
    length = len(ele)-2
    print(ele[0]+str(length)+ele[-1])
  else:
    print(ele)