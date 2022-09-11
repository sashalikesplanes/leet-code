class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list_sorted = sorted([char for char in s])
        t_list_sorted = sorted([char for char in t])
        if len(s_list_sorted) != len(t_list_sorted):
            return False

        return all(s_char == t_list_sorted[i] for i, s_char in enumerate(s_list_sorted))

       
