def myPow(x: float, n: int) -> float:
    res = 1
    if n < 0:
        x, n = 1 / x, -n
    while n != 0:
        if n % 2 == 1: res = res * x
        x = x * x
        n = n >> 1
    
    return res