def capitalizewords(arr):
    result = []
    if len(arr) == 0:
        return result
    else:
        for i in range(len(arr)):
            result.append(arr[i].upper())
        return result


