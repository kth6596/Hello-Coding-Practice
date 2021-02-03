def counting(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    bigger = [i for i in arr[1:] ]
    return [pivot] + counting(bigger)
print(counting([1,3,5,7]))
