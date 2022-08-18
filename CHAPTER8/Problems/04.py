 def sum_recursive(n):
    if n<=1:
        return n
    return n+sum_recursive(n-1)

num =16
print("The sum is: ", sum_recursive(num))
   
 