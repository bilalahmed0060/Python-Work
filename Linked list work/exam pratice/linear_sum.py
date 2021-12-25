def linear_sum(A,n):
    if n == 0:
        return 0
    else:
        return linear_sum(A,n-1)+A[n-1]