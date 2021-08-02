# 1. 
# bubble sort doesn't return anything since there is no 'return' statement, a possible fix for this would 
# be to pass the list by reference and not by value so that it modifies the actual address and not a copy of it. 
# - ignore the above just found out you can't pass by reference in python 

# 2.
# K starts at 1, so that the if statement right after it is able to function properly, as it checks behind it(-1 of it's position)every time
# if it started at 0, then the first index would go to '-1' which would give an out of bounds error 

# 3. + 4.

def bubblesort(list):
    nSwaps = 0 
    for i in range(len(list) - 1):
        for j in range(1, len(list) - i ): # fixes second loop doing too much work ,  the -i on len(list)
            if list[j] < list[j-1]:
                temp = list[j]
                list[j] = list[j - 1]
                list[j - 1] = temp
                nSwaps += 1
        if nSwaps == 0 :  # detect early sorting 
            break
    
    return list

mylist = [5,4,3,2,1,6,4,7,4,7]
my_sorted_list = bubblesort(mylist)
print(my_sorted_list)



# 5.  TO_FINISH

def lessthan(x,y):
    return x < y 
def evenfirst(list, x,y):
    if x % 2 == 0:
        pass
        

def bubblesortfun(list, comp_func):
    nSwaps = 0 
    for i in range(len(list) - 1):
        for j in range(1, len(list) ): # fixes second loop doing too much work ,  the -i on len(list)
            if list[j] < list[j-1]:
                comp_func(list, list[j], list[j-1])
        if nSwaps == 0 :  # detect early sorting 
            break
    
    return list

print(bubblesortfun(mylist, evenfirst))