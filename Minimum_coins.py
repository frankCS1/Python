def make_change(coin_vals, change):#The function
    minimum = [float('inf')] * (change + 1)#Table created to store the minimum number of coins needed for amount change
    minimum[0] = 0  #Starting, since no coins are required if there isn't any change

    coin_used = [[] for c in range(change + 1)] #Store coins used for change

    for coin in coin_vals: #Iterates each coin value
        for amount in range(coin, change + 1):#Updates change amounts
            if minimum[amount - coin] + 1 < minimum[amount]:
                minimum[amount] = minimum[amount - coin] + 1#Updates the table
                coin_used[amount] = coin_used[amount - coin] + [coin]

    return minimum[change], coin_used[change] #Minimum numbers of coins required

min_coins, coins_used = make_change([1, 5, 8], 11)#Testing function with the given values

print("Minimum coins needed:", min_coins, "and the coins used were:", coins_used)#The example


