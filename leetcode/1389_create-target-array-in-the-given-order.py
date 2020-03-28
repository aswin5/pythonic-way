""""Given two arrays of integers nums and index. Your task is to create target array under the following rules:

    Initially target array is empty.
    From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
    Repeat the previous step until there are no elements to read in nums and index.

Return the target array.

It is guaranteed that the insertion operations will be valid.

 

Example 1:

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

Example 2:

Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]
Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]

Example 3:

Input: nums = [1], index = [0]
Output: [1]

 

Constraints:

    1 <= nums.length, index.length <= 100
    nums.length == index.length
    0 <= nums[i] <= 100
    0 <= index[i] <= i

"

Returns:
    [type] -- [description]
"""


def createTargetArray(nums, index):
    viva = dict()
    for x in range(len(index)):
        if index[x] in viva:
            temp = viva[index[x]]
            viva[index[x]] = nums[x]
            z = list(viva.keys())
            z.sort()
            z.reverse()
            for k in z:
                if k > index[x]:
                    viva[k+1] = viva[k]
            viva[index[x] + 1] = temp
        else:
            viva[index[x]] = nums[x]
    return list(viva.values())



# others
def other_1(nums, index):
    arr = []
    for i in range(len(nums)):
        if index[i] == i: 
            arr.append(nums[i])
        else:
            arr = arr[:index[i]] + [nums[i]] + arr[index[i]:]
    return arr    



# others
def other_2(nums, index):
    data = []
    for i in range(0, len(nums)):
        data.insert(index[i], nums[i])
    return data    


nums = [0,1,2,3,4]
index = [0,1,2,2,1]
target = [0,4,1,3,2]

print(other_2(nums, index))