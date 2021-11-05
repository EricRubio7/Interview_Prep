#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Python3 Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
                
#Time complexity O(n^2): Because of the nested loop
#Space complexity O(1): Because the space required does not depend on the size of the input array

#Lessons: 
#1) Arrays and nested loops will be useful for a quick brute force approach
#2) Thinking of the problem as and algebra problem will give a quick solution: x + y = target
#3) We can use range in python to create a sequence of numbers, and use it for iterations
