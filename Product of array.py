def productofarray(arr):
    if len(arr) == 0:
        return 1
    else:
        prod = 1
        for i in range(len(arr)):
            prod = prod * arr[i]
    return prod

