# Uses python3

import math

def calc_modulo_m_of_fib(n, m):
    """Calculates the last digit of nth fibonacci number modulo m"""

    remainder = n % get_pisano_period(m)
    res = remainder

    fib_prev_prev, fib_prev = (0, 1)

    for index in range(1, remainder):
        res = (fib_prev_prev + fib_prev) % m
        fib_prev_prev = fib_prev
        fib_prev = res

    return res % m

def get_pisano_period(m):
    a, b = (0, 1)
    c = a + b

    for i in range(0, m*m):
        c = (a + b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            return i + 1

input = input()
n, m = map(int, input.split())
print(calc_modulo_m_of_fib(n, m))
