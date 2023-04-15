'''
Use a dictionary to record the value and index of the current number, 
the value is key, and the index is val. 
If target-curr_num is in the key of the dictionary, 
return the current index and the value corresponding to the key
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for index, num in enumerate(nums):
            if num in a:
                return [index, a[num]]
            else:
                a[target-num] = index
