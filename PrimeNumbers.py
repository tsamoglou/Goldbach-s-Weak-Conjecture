from math import sqrt


def isPrime(number):
    if number == 2:
        return True
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


print("Give an Prime number:")
x = int(input())

for j in range(2, x - 2):
    if isPrime(j):
        for k in range(j, x - j):
            if isPrime(x - j - k):
                if isPrime(k) and x - j + k == x:
                    print(j, " ", k, " ", x - j - k)
