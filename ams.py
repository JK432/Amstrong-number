def ams(n,m):
  l=[]
  
  for i in range(n,m):
    sum = 0


    temp = i
    while temp > 0:
      digit = temp % 10
      sum += digit ** 3
      temp //= 10


    if i == sum:
      l.append(i)
  v=len(l)
  for i in l[:v-1]:
    print(i,end=" ")
  print(l[v-1])

  
