from math import factorial


n = int(input("Enter the number: "))
fac = 1
for i in range(1, n+1):
    fac = fac*i
print(fac)


