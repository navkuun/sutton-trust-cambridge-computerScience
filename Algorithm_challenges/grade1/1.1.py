N = 5000
memo = [-1] * N
memo[0] = 0
memo[1] = 1


def fib_dyanmic_programming(n):
    if memo[n] != -1:
        return memo[n]

    memo[n] = fib_dyanmic_programming(n - 1) + fib_dyanmic_programming(n - 2)

    return memo[n]


nth_term = int(input("Please enter the term you would like : "))
print(f"The term you want is {fib_dyanmic_programming(nth_term)}")

# BRUTEFORCE FIB


def fib_bruteforce(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_bruteforce(n - 1) + fib_bruteforce(n - 2)


nth_term1 = int(input("Please enter the terms you would like : "))
print(f"The term you want is {fib_bruteforce(nth_term1)}")

# VERY NOTICABLE SPEED DIFFERENCE AS VALUE OF NTH TERM INCREASES, SHOWS 
# HOW DYNAMIC PROGRAMMING OPTIMISES THE PROBLEM