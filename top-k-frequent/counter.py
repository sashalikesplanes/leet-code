# O(n)
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [el for el, count in count.most_common(k)]

sol = Solution()
print(sol.topKFrequent([3, 0, 1, 0], 2))
