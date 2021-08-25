def karatsuba(x, y):
    if len(str(x)) ==1 or len(str(y)) ==1:
        return x*y
    
    max_num = max(len(str(x)), len(str(y)))
    n = max_num //2

    a = x // (10**n)
    b = x % (10**n)
    c = y // (10**n)
    d = y % (10**n)

    z0 = karatsuba(a, c)
    z1 = karatsuba(b, d)
    z2 = karatsuba((a+b), (c+d))

    return (z0 * 10**(2*n) + z1 + (z2-z1-z0)*(10**n))


print(karatsuba(12, 34))
print(karatsuba(1234, 5678))