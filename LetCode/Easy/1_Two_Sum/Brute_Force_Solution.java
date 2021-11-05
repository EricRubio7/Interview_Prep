/*Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Java Solution
*/


class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++){
            for(int j = i + 1; j < nums.length; j++){
                if (nums[j] == target - nums[i]) {
                    return new int [] {i , j};
                }
            } 
        }       
    //In case there is no solution, we'll just return null
    return null;
    }
}

/*
Time complexity O(n^2): Because of the nested loop
#Space complexity O(1): Because the space required does not depend on the size of the input array

Lessons: 
1) Arrays and nested loops will be useful for a quick brute force approach
2) Thinking of the problem as and algebra problem will give a quick solution: x + y = target
3) Java sintax seems similar to C (... I think so)
4) Java uses methods and needs type definitions

*/
