from functools import lru_cache


@lru_cache
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 501):
    print(i, '::', fibonacci(i))
