from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_ints = set()
        for num in nums:
            if num in seen_ints:
                return True
            seen_ints.add(num)
        return False

sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]))
