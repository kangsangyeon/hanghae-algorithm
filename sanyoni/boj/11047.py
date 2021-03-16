import sys

coin_count, money = sys.stdin.readline().rstrip().split()
coin_count = int(coin_count)
money = int(money)

coins_list = [int(sys.stdin.readline().rstrip()) for i in range(coin_count)]
coins_list.sort()

remaining_money = money
used_coins_count = 0
for i in reversed(range(0, len(coins_list))):
    current_coin = coins_list[i]
    if remaining_money >= current_coin:
        coins_count_to_use = remaining_money // current_coin

        remaining_money -= current_coin * coins_count_to_use
        used_coins_count += coins_count_to_use

        if remaining_money == 0:
            break

print(used_coins_count)