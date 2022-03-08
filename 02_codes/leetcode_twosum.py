import os
import pandas as pd
import numpy as np

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i == j:
                    break
                if (nums[i] + nums[j]) == target:
                    result = [i, j]
                    print(result)
                    break


a = Solution()
a.twoSum([3, 2, 4], 6)
