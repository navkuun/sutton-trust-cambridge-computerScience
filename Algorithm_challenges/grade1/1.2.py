print("Please enter a list of coin denominations seperated by a space : ")
denominations = [int(d) for d in input().split()]
value = int(input("Please enter the value that you would like to calculate : "))
# Use the biggest coin available each time

coins = []
# get the maximum possible coin
denominations.sort(reverse=True)
if denominations[-1] != 1:  # found out that if you don't have 1 could be infinite loop
    denominations.append(1)
while value >= 0:
    x = 0
    for i in range(len(denominations)):
        if denominations[i] <= value:
            x = denominations[i]
            break
    if value - x < 0:
        break
    value -= x
    coins.append(x)

print(f"The coins that were used : {coins}, and the number of coins {len(coins)}")
