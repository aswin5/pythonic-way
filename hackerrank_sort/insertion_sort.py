# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for x in range(1, len(arr)):
        key = arr[x]

        # Insert arr[x] into sorted sequence
        i = x-1
        
        while i>=0 and arr[i]> key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
        print(' '.join([str(x) for x in arr]))
        
arr = [8, 7, 6, 5, 4, 3, 2, 1]
n = len(arr)

insertionSort2(n, arr)
