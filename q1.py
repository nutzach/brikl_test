import sys

def minCoins(coins, V):
    table = [sys.maxsize] * (V + 1)
    table[0] = 0
    for i in range(1, V + 1):
        for coin in coins:
            if coin <= i:
                sub_res = table[i - coin]
                if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                    table[i] = sub_res + 1
    if table[V] == sys.maxsize:
        return -1
    return table[V]
