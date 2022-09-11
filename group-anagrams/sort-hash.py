from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            # Every sorted anagram will match
            letter_count = [0] * 26
            for char in s:
                letter_count[ord(char) - ord('a')] += 1

            current_group = groups.get(tuple(letter_count), [])
            current_group.append(s)
            groups[tuple(letter_count)] = current_group

        return [group for group in groups.values()]


sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams(["bdddddddddd","bbbbbbbbbbc"]))

