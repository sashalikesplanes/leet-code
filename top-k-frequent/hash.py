from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(lambda: 0)
        # O(n)
        for num in nums:
            hash_map[num] += 1

        prev_bests = [(None, 0)] * k
        for el, count in hash_map.items():
            for i, (best_el, best_count) in enumerate(prev_bests):
                if count > best_count:
                    prev_bests.pop(-1)
                    prev_bests.insert(i, (el, count))
                    break


        return [el for el, count in prev_bests]



sol = Solution()
print(sol.topKFrequent([5,2,5,3,5,3,1,1,3], 2))

