#1
def biggie_size(lst):
  for i in range(len(lst)):
    if lst[i] > 0:
      lst[i]="big"
  return lst
print(biggie_size([-1, 3, 5, -5]))

#2

def count_positives(lst):
    count = 0
    for i in lst:
        if i > 0:
            count += i
        lst[-1] = count
    return lst 
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))    


#3
def sum_total(lst):
  sum=0
  for i in lst:
    sum+=i
  return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

# 4
def average(lst):
  avg=0
  for values in lst :
    avg+=values
  x=avg/len(lst)
  return x
print(average([1,2,3,4]))

# 5
def length(lst):
  length=0
  for i in lst:
    length+=1
  return length
print(length([37,2,1,-9]))
print(length([]))


# 6
def minimum(lst):
  if len(lst)==0:
    return False
  min_num=lst[0]
  for num in lst:
    if num<min_num:
      min_num=num
  return min_num
print(minimum([37,2,1,-9]))
print(minimum([]))


#7
def maximum(lst):
  if len(lst)==0:
    return False
  max_num=lst[0]
  for num in lst:
    if num>max_num:
      max_num=num
  return max_num
print(maximum([37,2,1,-9]))
print(maximum([]))

#8

def ultimate_analysis(lst):
  sumTotal=sum_total(lst)
  avg=average(lst)
  mini=minimum(lst)
  maxi=maximum(lst)
  leng=length(lst)
  
  dic_analysis = {
    'sumTotal':sumTotal,
    'average':avg,
    'minimum':mini,
    'maximum':maxi,
    'length':leng
    }
  return dic_analysis
print(ultimate_analysis([37,2,1,-9]))

#9

def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        temp = lst[left]
        lst[left] = lst[right]
        lst[right] = temp
        left += 1
        right -= 1
    return lst
print(reverse_list([37, 2, 1, -9]))
