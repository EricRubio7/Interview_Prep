class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #Create hashmap
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return[i, hashmap[complement]]
            hashmap[nums[i]] = i 
                
#Time complexity O(n): Because we only need one loop and the hash table reduces lookup to O(1)
#Space complexity O(n): Because the space required depends on the number of elements in the array as they are stored in the hashmap

#Lessons: 
#1) Python dictionaries can be used as hashmaps
#2) Hashmaps introduce a tradeoff of space for time

