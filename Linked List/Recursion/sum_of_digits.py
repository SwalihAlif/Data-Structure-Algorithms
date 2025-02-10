# example
# 472 / 10 = 47 -------------- Remainder 2
# 47 / 10 = 4 ---------------- Remainder 7
# 4 / 10 = 0 ----------------- Remainder 4 (answer 13)

# in python // - quotient
#           %  - remainder

def sum_digits(n):
    remainder = n % 10
    if n // 10 == 0:
        return remainder
    return remainder + sum_digits(n // 10)

print(sum_digits(191))

