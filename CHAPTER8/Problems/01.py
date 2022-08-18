def m(a, b, c):

    if(a>b and a>c):
        max=a
    elif(b>a and b>c):
        max=b
    elif(c>a and c>b):
        max=c
    return max

max = m(3,87, 65)
print("Greatest of three: "+ str(max))

