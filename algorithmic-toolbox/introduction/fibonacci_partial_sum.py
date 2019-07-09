# Uses python3
import sys

def calc_last_digit_of_fib_partial_sum(m, n):
    """Calculates the last digit of nth fibonacci number"""

    if n == 0:
        return 0
    elif n == 1:
        return 1

    pisano_period = get_pisano_period(10)
    remainder1 = m % pisano_period
    remainder2 = n % pisano_period
    res = remainder1

    fib_prev_prev, fib_prev = (0, 1)
    sum = 1 if remainder1 <= 1 else 0

    for index in range(2, remainder2+1):
        res = (fib_prev_prev + fib_prev) % 10
        fib_prev_prev = fib_prev
        fib_prev = res
        if index >= remainder1:
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

def fib(m, n):
    return calc_last_digit_of_fib_partial_sum(m, n)

input = input()
from_, to = map(int, input.split())
print(fib(from_, to))
