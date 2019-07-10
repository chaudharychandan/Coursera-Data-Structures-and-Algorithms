# Uses python3

def get_change(m):
    num_of_coins = 0
    coins = [10, 5, 1]
    index = 0

    while m > 0:
        coin = coins[index]
        count = m // coin
        num_of_coins += count
        m = m - (count*coin)
        index = index + 1
    return num_of_coins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
