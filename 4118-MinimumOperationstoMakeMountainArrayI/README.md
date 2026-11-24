You are given an integer array nums of length n.

In one operation, you may increment or decrement any element of nums by 1.

All elements of nums must remain positive (at least 1) after every operation.

An array is called a mountain array if there exists an index peak such that 0 < peak < n - 1 and:


	nums[0] < nums[1] < ... < nums[peak]
	nums[peak] > nums[peak + 1] > ... > nums[n - 1]


Return the minimum number of operations required to transform nums into a mountain array. If it is impossible, return -1.

 
Example 1:


Input: nums = [2,2,3]

Output: 2

Explanation:

​​​​​​​One optimal way is to:


	Increment nums[1] by 1 and decrement nums[2] by 1.
	The resulting array is [2, 3, 2], which is a mountain array with peak = 1.
	Therefore, the total number of operations is 1 + 1 = 2.



Example 2:


Input: nums = [9,4,9]

Output: 6

Explanation:

One optimal way is to:


	Increment nums[1] by 1 six times.
	The resulting array is [9, 10, 9], which is a mountain array with peak = 1.
	Therefore, the total number of operations is 6.



Example 3:


Input: nums = [5,7,7,4]

Output: 1

Explanation:

One optimal way is to:


	Decrement nums[1] by 1.
	The resulting array is [5, 6, 7, 4], which is a mountain array with peak = 2.
	Therefore, the total number of operations is 1.



Example 4:


Input: nums = [1,2]

Output: -1

Explanation:

A mountain array must have a peak with at least one element on each side. Since n = 2 and operations do not change the array's length, forming a mountain array is impossible.


 
Constraints:


	1 <= n == nums.length <= 1000
	1 <= nums[i] <= 1000

