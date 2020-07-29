def genPrimes():
    ans = 2
    primenums = [2]
    yield ans
    while True:
        ans += 1
        remainders = []
        for i in primenums:
            remainders.append(ans % i)
        if 0 not in remainders:
            primenums.append(ans)
            yield ans