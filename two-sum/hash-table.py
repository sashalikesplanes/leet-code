# Hash map approach, should get O(N)
from typing import List
from math import floor

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = LinkedListNode(value)
        else:
            next_node = self.head
            while next_node.next:
                next_node = next_node.next

            next_node.next = LinkedListNode(value)

    def values(self):
        output = []
        next_node = self.head
        while next_node:
            output.append(next_node.value)
            next_node = next_node.next
        return output

class LinkedListNode:
    def __init__(self, value):
        self.next = None
        self.value = value

class HashMap:

    def __init__(self, hash_f, map_size):
        self.MAP_SIZE = map_size
        self.arr = [LinkedList()] * self.MAP_SIZE 
        self.hash_f = hash_f

    def insert(self, key_value):
        hash_code = self.hash_f(key_value[0])
        idx = hash_code % self.MAP_SIZE
        self.arr[idx].append(key_value)

    def lookup(self, key):
        hash_code = self.hash_f(key)
        idx = hash_code % self.MAP_SIZE
        for key_value in self.arr[idx].values():
            if key_value[0] == key:
                return key_value[1]
        return None

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = HashMap(lambda x: x, len(nums))

        # Fill hash map
        for i, num in enumerate(nums):
            required = target - num
            index_found = hash_map.lookup(required)
            if index_found is not None and index_found != i:
                return [i, index_found]
            hash_map.insert((num, i))

        i = len(nums) - 1
        required = target - nums[i]
        index_found = hash_map.lookup(required)
        if index_found and index_found != i:
            return [i, index_found]

solution = Solution()



list = LinkedList()
# print(solution.twoSum([i for i in range(1001)], 1999))
# print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([2, 7, 11, 15], 9))

hash_map = HashMap(lambda x: x, 5)
hash_map.insert((0, 0))
hash_map.insert((1, 6))
hash_map.insert((2, 5))
hash_map.insert((3, 5))
hash_map.insert((6, 5))

# print(hash_map.lookup(6), hash_map.lookup(1), hash_map.lookup(-1), hash_map.lookup(3), )
