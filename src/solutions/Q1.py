#two sum
from typing import List, Tuple, Dict, TextIO
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in d.keys():
                return i, d[temp]
            d[nums[i]]=i
        return None


l = [1, 2, 3, 4, 5, 6, 7]
target = 13
res=Solution1().twoSum(l, target)
print(res)
