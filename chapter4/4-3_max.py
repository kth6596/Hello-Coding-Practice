def max(arr):
    if len(arr) < 2:
        return arr
    else:
      pivot =  arr[0]
      bigger = [i for i in arr[1:] if i > pivot]

      return max(bigger)
print(max([1,3,5,7]))
