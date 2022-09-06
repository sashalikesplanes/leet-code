# Works but it is NlogN as the sort is required
from typing import List
from collections import namedtuple
from math import floor

ValueIndex = namedtuple('ValueIndex', ['value', 'index'])
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_list = self.sort(nums)
        for i, num in enumerate(nums):
            match_required = target - num
            idx = self.find_index_sorted(sorted_list, match_required)
            if idx != -1 and i != idx: 
                return [i, idx]


    def sort(self, nums: List[int]) -> List[ValueIndex]:
        # convert array to array of ValueIndecies before sorting
        unsorted = [ValueIndex(value = num, index = i) for i, num in enumerate(nums)]
        return self._merge_sort_value_index(unsorted)
    
    def _merge_sort_value_index(self, nums: List[ValueIndex]) -> List[ValueIndex]:
        # base case if array is length 0
        if len(nums) == 0 or len(nums) == 1:
            return nums

        midpoint = floor(len(nums) / 2)
        return self._merge(self._merge_sort_value_index(nums[0:midpoint]), self._merge_sort_value_index(nums[midpoint:]))

    def _merge(self, nums1: List[ValueIndex], nums2: List[ValueIndex]) -> List[ValueIndex]:
        output = []
        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0].value > nums2[0].value:
                output.append(nums2.pop(0))
            else:
                output.append(nums1.pop(0))

        while len(nums1) > 0:
            output.append(nums1.pop(0))

        while len(nums2) > 0:
            output.append(nums2.pop(0))

        return output


    def find_index_sorted(self, sorted_nums: List[ValueIndex], target: int) -> int:
        # Return -1 if not found
        if len(sorted_nums) == 0:
            return -1

        midpoint = len(sorted_nums) // 2
        if sorted_nums[midpoint].value == target:
            return sorted_nums[midpoint].index

        left_index = self.find_index_sorted(sorted_nums[0:midpoint], target)
        right_index = self.find_index_sorted(sorted_nums[midpoint + 1:], target)
        if left_index != -1: return left_index
        elif right_index != -1: return right_index
        else: return -1

solution = Solution()

print(solution.sort([2, 1, 3]))

print([val for (val, idx) in solution.sort([2, 3, 7, 1])])
print([val for (val, idx) in solution.sort([54, 5, 4, 2, 7, 3, 2, 7, 9, 1, 6, 3, 9, 0])])
sorted_list = solution.sort([54, 5, 4, 2, 7, 3, 2, 7, 9, 1, 6, 3, 9, 0])
print(solution.find_index_sorted(sorted_list, 4))
print(solution.find_index_sorted(sorted_list, 3))
print(solution.find_index_sorted(sorted_list, 54))
print(solution.find_index_sorted(sorted_list, 69))
print(solution.find_index_sorted(sorted_list, -10))

print(solution.twoSum([i for i in range(10001)], 19999))
print(solution.twoSum([3, 2, 4], 6))
