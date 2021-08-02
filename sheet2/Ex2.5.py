import math

pi = math.pi
def approx_sin(x):   
    ans = 0 
    for i in range(0, 16): # n = 15 since range is inclusive

        f = math.factorial((2*i) + 1)
        t = x**((2*i) + 1)
        b = (-1) ** i
        ans += b * (t / f)
        
    return ans

print(approx_sin((3 * pi) / 2)) # roughly -1

def terms_close(x):
    ans = 0 
    i = 0
    while(abs(ans - (math.sin((3*pi)/2))) >= (1e-8)):
        f = math.factorial((2*i) + 1)
        t = x**((2*i) + 1)
        b = (-1) ** i
        ans += b * (t / f)
        i += 1
    
    print(i + 1)

print(terms_close((3*pi) / 2)) # 13 terms




    

