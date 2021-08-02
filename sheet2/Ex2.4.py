def primez(z): # prime number only divsible by itself and 1
    if(z == 2): 
        return [2]
    prime_nums = []
    for i in range(3,z+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else: 
            prime_nums.append(i)

    return prime_nums

print(primez(15))
