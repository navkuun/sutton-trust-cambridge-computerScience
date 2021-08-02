def list_max(arr):
    arr.sort()
    return arr[-1]

print(list_max([5,6,3,2,5,100])) # OUT: 100