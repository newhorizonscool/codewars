def f(n:int) -> int:
    sum = 0
    m = 10**9 + 7
    for k in range(n+1):
        sum = sum + 2**k*k**2
    sum = sum % m
    return sum

print(f())