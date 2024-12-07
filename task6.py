def f(n):
    if n== 1:
        return  1
    else:
        n = f(n-1) + 2 ** (n-1)
        return n
n = 12
print(f(n))

