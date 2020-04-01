
"""
Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


Input: [2,2,1]
Output: 1
"""

def singleNumber(nums):
    viva = dict()

    for x in range(len(nums)):
        if nums[x] in viva:
            viva[nums[x]] += 1
        else:
            viva[nums[x]] = 1
    for key, value in viva:
        if value == 1:
            return key

        