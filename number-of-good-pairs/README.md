<h1><a href="https://github.com/eddiephiri/competitive-programming/blob/main/number-of-good-pairs/">1512. Number of Good Pairs</a></h1>

<a href="https://leetcode.com/problems/number-of-good-pairs/submissions/1171354651/">LeetCode Submission</a>

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
