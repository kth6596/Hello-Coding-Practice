def sum(arr):
    total = 0
    if len(arr) < 1:
        return arr
    for i in arr:
        total = total + i
    return total
print(sum([1,3,5,7]))
