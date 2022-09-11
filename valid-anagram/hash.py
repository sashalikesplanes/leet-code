class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        # Fill hashmap with first string
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

        # Empty hash map 
        for char in t:
            if char in hash_map:
                hash_map[char] -= 1
            else:
                return False

        # Check if all of hash map is at 0
        return all(value == 0 for value in hash_map.values())

sol = Solution()
sol.isAnagram('anagram', 'nagaram')
