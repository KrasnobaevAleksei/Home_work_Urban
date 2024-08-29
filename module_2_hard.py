list_  = []
n = int(input('Число из первой вставки : '))

for i in range(1, n):
    for j in range(i+1, n):
        if n % (i+j) == 0:
            list_.append(i)
            list_.append(j)
print(*list_)
