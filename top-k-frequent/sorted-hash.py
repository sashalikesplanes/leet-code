from collections import defaultdict
# O(nlogn)
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(lambda: 0)
        # O(n)
        for num in nums:
            hash_map[num] += 1
        # O(nlogn)
        most_frequent = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)
        return [el for el, count in most_frequent[0:k]]


sol = Solution()
print(sol.topKFrequent([3, 0, 1, 0], 2))

