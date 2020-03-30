# 1380. Lucky Numbers in a Matrix


"""Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]

 

Constraints:

    m == mat.length
    n == mat[i].length
    1 <= n, m <= 50
    1 <= matrix[i][j] <= 10^5.
    All elements in the matrix are distinct.

"""


def luckyNumbers(matrix):
    viva = dict()
    for x in range(len(matrix)):
        if 'min' in viva:
            viva['min'].append(min(matrix[x]))
        else:
            viva['min'] = [min(matrix[x])]
        for y in range(len(matrix[x])):
            if y not in viva:
                viva[y] = [matrix[x][y]]
            else:
                viva[y].append(matrix[x][y])
    for x in range(len(matrix[0])):
        if 'max' not in viva:
            viva['max'] = [max(viva[x])]
        else:
            viva['max'].append(max(viva[x]))
    return list(set(viva['min']) & set(viva['max']))



# vida = [[3,7,8],[9,11,13],[15,16,17]]
vida = [[7,8],[1,2]]
# vida = [[36376,85652,21002,4510],[68246,64237,42962,9974],[32768,97721,47338,5841],[55103,18179,79062,46542]]
output = []

print(luckyNumbers(vida))



# other
def other(matrix):
    minrow = {min(r) for r in matrix}
    maxcol = {max(c) for c in zip(*matrix)} 
    return list(minrow & maxcol)