def power(x,n):
    ans = x
    for i in range(1,n):
        ans *= x    
    return ans 

print(power(5,2)) # OUT: 25
