def positiveinterger(n):
    if n<1:
        return 0
    else:
        return n + positiveinterger(n-2)
print(positiveinterger(10))


