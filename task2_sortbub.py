import numpy as np

li = np.random.randint(-10,20,(20))
print(li)
n=1
while n < len(li):
     for i in range(len(li)-n):
          if li[i] > li[i+1]:
               li[i],li[i+1] = li[i+1],li[i]
     n += 1
print(li)
