from collections import Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []

        while len(strs) > 0:
            first_str = strs[0]
            group = [first_str]
            strs.remove(first_str)
            for other_str in strs[:]:
                if self._isAnagram(first_str, other_str):
                    group.append(other_str)
                    strs.remove(other_str)
                    print(strs, group)
            groups.append(group)
        return groups
                    
            # remove string and add it to a new group
            # for this string, search for all anagrams, remove them and add to new group
            # add new group to groups

    def _isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        
        
