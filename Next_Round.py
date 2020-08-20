n, k =map(int,input().split())
arr=list()
count=0
arr = map(int,input().split())
arrayy = list(arr)
try:
  advance_pos = arrayy[k-1]
  for i in arrayy:
    if i >= advance_pos and i!=0:
      count+=1
    elif i==0:
      break
  print(count)
except IndexError:
  print('error')

'''
8 5
10 9 8 7 7 7 5 5'''