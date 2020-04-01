"""
922. Sort Array By Parity II

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

 

Note:

    2 <= A.length <= 20000
    A.length % 2 == 0
    0 <= A[i] <= 1000
"""



def sortArrayByParityII(A):
    viva = dict()
    viva['even'] = []
    viva['odd'] = []

    for x in range(len(A)):
        if x%2 == 0 and A[x] %2 != 0:
            viva['odd'].append([x, A[x]])
            A[x] = 'i'
        elif x%2 != 0 and A[x]%2 == 0:
            viva['even'].append([x, A[x]])
            A[x] = 'i'
    for x in range(len(viva['even'])):
        A[viva['even'][x][0]] = viva['odd'][x][1]
        A[viva['odd'][x][0]] = viva['even'][x][1]
    return A
        

    return int


Input= [4,2,5,7]
Output= [4,5,2,7]

print(sortArrayByParityII(Input))