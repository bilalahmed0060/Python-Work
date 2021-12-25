def binary_search(data,target,low,high):
    if low>high:
        return False
    else:
        mid = (low+high)//2
        if target==data[mid]:
            return True
        elif target<data[mid]:
            return binary_search(data,target,low,mid-1)
        else:
            return binary_search(data,target,mid+1,high)

data = [1,2,3,4,5,6,7,9,10,11,12]
low = 0
high = len(data)-1
