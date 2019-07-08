# Uses python3
import sys

def calc_last_digit_of_fib_series_sum(n):
    """Calculates the last digit of sum of n fibonacci number"""

    remainder = n % get_pisano_period(10)

    if remainder == 0:
        return 0
    elif remainder == 1:
        return 1

    res = remainder

    fib_prev_prev, fib_prev = (0, 1)
    sum = 1

    for index in range(1, remainder):
        res = (fib_prev_prev + fib_prev) % 10
        fib_prev_prev = fib_prev
        fib_prev = res
        sum = (sum + res) % 10

    return sum

def get_pisano_period(m):
    a, b = (0, 1)
    c = a + b

    for i in range(0, m*m):
        c = (a + b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            return i + 1

def fib(n):
    return calc_last_digit_of_fib_series_sum(n)

input = input()
n = int(input)
print(fib(n))
