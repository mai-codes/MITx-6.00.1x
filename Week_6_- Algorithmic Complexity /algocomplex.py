def foo(L):
    val = L[0]
    print(val)
    print(L[val])
    while (True):
        val = L[val]

a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]

foo(c)