def sum_digit(x):
    if x == 0:
        return 0
    else:
        return x%10 + sum_digit(int(x/10))
print(sum_digit(251))