def binary_recursive_sum(data, low, high):
    if low > high:
        return 0
    elif low == high:
        return data[low]
    else:
        mid = (low+high) //2
        return binary_recursive_sum(data, low, mid) +binary_recursive_sum(data, mid+1, high)
