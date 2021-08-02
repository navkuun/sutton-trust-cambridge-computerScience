
def evens(k):
    even_list = [d for d in range(0,k) if d % 2 == 0]
    return even_list

print(evens(5)) 
# OUT : [0,2,4]