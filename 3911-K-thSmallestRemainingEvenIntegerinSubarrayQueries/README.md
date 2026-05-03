You are given an integer array nums where nums is strictly increasing.

You are also given a 2D integer array queries, where queries[i] = [li, ri, ki].

For each query [li, ri, ki]:


	Consider the subarray nums[li..ri]
	From the infinite sequence of all positive even integers: 2, 4, 6, 8, 10, 12, 14, ...
	Remove all elements that appear in the subarray nums[li..ri].
	Find the kith smallest integer remaining in the sequence after the removals.


Return an integer array ans, where ans[i] is the result for the ith query.

 
Example 1:


Input: nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]

Output: [2,6,6]

Explanation:

iqueries[i]nums[li..ri]Removed
			EvensRemaining
			Evenskians[i]0[0, 2, 1][1, 4, 7][4]2, 6, 8, ...121[1, 1, 2][4][4]2, 6, 8, ...262[0, 0, 3][1][]2, 4, 6, ...36

Thus, ans = [2, 6, 6].


Example 2:


Input: nums = [2,5,8], queries = [[0,1,2],[1,2,1],[0,2,4]]

Output: [6,2,12]

Explanation:

iqueries[i]nums[li..ri]Removed
			EvensRemaining
			Evenskians[i]0[0, 1, 2][2, 5][2]4, 6, 8, ...261[1, 2, 1][5, 8][8]2, 4, 6, ...122[0, 2, 4][2, 5, 8][2, 8]4, 6, 10, 12, ...412

Thus, ans = [6, 2, 12].


Example 3:


Input: nums = [3,6], queries = [[0,1,1],[1,1,3]]

Output: [2,8]

Explanation:

iqueries[i]nums[li..ri]Removed
			EvensRemaining
			Evenskians[i]0[0, 1, 1][3, 6][6]2, 4, 8, ...121[1, 1, 3][6][6]2, 4, 8, ...38

Thus, ans = [2, 8].


 
Constraints:


	1 <= nums.length <= 105
	1 <= nums[i] <= 109
	nums is strictly increasing
	1 <= queries.length <= 105
	queries[i] = [li, ri, ki]
	0 <= li <= ri < nums.length
	1 <= ki <= 109​​​​​​​

