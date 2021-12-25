#iteration
def power1(x,n):
    result =1
    for i in range(n):
        result = result*x
    return result


#recursion
def power2(x,n):
    if n==0:
        return 1
    else:
        return x*power2(x,n-1)