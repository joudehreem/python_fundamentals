#1
for i in range(151):
  print(i)

#2
for x in range(5,1001,5):
  print(x)

#3
for j in range(1,101):
  if j%10==0:
    print("Coding Dojo")
  elif j%5==0:
    print("Dojo")
  else:
    print(j)
#4
odd_sum=0
for k in range(1,50000,2):
  odd_sum+=k
print(f"The final {odd_sum}")
for n in range(2018,0,-4):
  print(n)
  
#5
lowNum=2
highNum=9
mult=3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)