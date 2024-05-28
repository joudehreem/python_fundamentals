lst=[]

#1
def countdown(number):
  lst  
  for i in range(number,-1,-1):
    lst.append(i)
  return  lst
print(countdown(5))

#2 again 
def  print_and_return (lst):
  print(lst[0])
  return lst[1]
print(print_and_return([1,2]))

#3
def first_plus_length (lst): 
  first_value=lst[0]
  length_lst=len(lst)
  result=first_value+length_lst
  return result    
print(first_plus_length([1,2,3,4,5]))

#4
def values_greater_than_second(lst):
  if len(lst)<2:
    return False
  else:
    second_value=lst[1]
    new_list = []
    for value in lst:
      if value > second_value:
        new_list.append(value)  
  return new_list
print(values_greater_than_second([5,2,3,2,1,4]))
print( values_greater_than_second([3]))

#5
def length_and_value(size,value):
  new_list=[value]*size
  return new_list
print(length_and_value(4,7))
print(length_and_value(6,2))
