"""

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

 

Constraints:

    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5
"""

def funcs(arr):
    viva = dict()
    for x in range(len(arr)):
        if x == len(arr) - 1:
            viva[x] = [-1]
        else:
            viva[x] = arr[x+1:len(arr)]
    return [max(value) for key, value in viva.items()]


vida = [17,18,5,4,6,1]
output = [18,6,6,6,1,-1]
print(funcs(vida))