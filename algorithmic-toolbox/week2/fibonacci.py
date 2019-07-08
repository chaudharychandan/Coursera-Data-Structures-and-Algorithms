# Uses python3
def calc_fib(n):
    """Calculates the nth fibonacci number"""

    cache = { 0: 0, 1: 1 }

    def fib(n):
        nonlocal cache

        if n in cache:
            return cache[n]
        res = fib(n-1) + fib(n-2)
        cache[n] = res

        return res
    
    return fib(n)
        

n = int(input())
print(calc_fib(n))
