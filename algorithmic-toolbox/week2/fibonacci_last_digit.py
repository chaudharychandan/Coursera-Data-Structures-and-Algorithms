# Uses python3
def calc_last_digit_of_fib(n):
    """Calculates the last digit of nth fibonacci number"""

    cache = { 0: 0, 1: 1 }

    def fib(n):
        nonlocal cache

        if n in cache:
            return cache[n]
        res = (fib(n-1) + fib(n-2)) % 10
        cache[n] = res
    
    for index in range(0, n+1):
        fib(index)

    return fib(n)

n = int(input())
print(calc_last_digit_of_fib(n))
