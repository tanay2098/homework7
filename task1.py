from random import seed
from random import randint

#Generate 20 random integers
lst=[]
# seed random number generator
seed(2020)
# generate some integers
for i in range(20):
	value = randint(100, 120)
	lst.append(value)

print(lst)

#To find the median
n = len(lst) 
lst.sort() 
  
if n % 2 == 0: 
    median1 = lst[n//2] 
    median2 = lst[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = lst[n//2] 
print("Median is: " + str(median))

#to find the mode
lst.sort()
lst2=[]
i = 0
while i < len(lst) : 
    lst2.append(lst.count(lst[i])) 
    i += 1

d1 = dict(zip(lst, lst2))
d2={k for (k,v) in d1.items() if v == max(lst2) } 
  
print("Mode(s) is/are :" + str(d2))
