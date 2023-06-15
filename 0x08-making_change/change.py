def change(coins, total):
    for i in range(total/coins[0]):
        change(coins, total - i * coins[0]
