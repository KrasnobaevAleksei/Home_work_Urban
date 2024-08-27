numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers_:
    isprime = True
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            isprime = False
            break
    if isprime:
            primes.append(i)
    else:
            not_primes.append(i)
print(not_primes)
print(primes)
