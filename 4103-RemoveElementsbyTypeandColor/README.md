You are given three integer arrays types, colors, and groupSize, where types and colors have length n, and groupSize has length m.


	types[i] represents the type of the element at index i.
	colors[i] represents the color of the element at index i.
	groupSize[t] represents the required number of elements in a removable group of type t.


In one operation, you may remove exactly groupSize[t] consecutive elements if all of them have type t and the same color.

After each removal, the remaining elements become adjacent again while maintaining their relative order.

Return true if it is possible to remove all elements using a sequence of valid operations. Otherwise, return false.

 
Example 1:


Input: types = [0,1,1,0], colors = [5,3,3,5] , groupSize = [2,2]

Output: true

Explanation:


	First, remove the consecutive elements at indices 1 and 2. Both elements have type 1, color 3, and the group size is equal to groupSize[1] = 2.
	The remaining sequence is: types = [0, 0], colors = [5, 5]
	Now remove the two remaining elements. They have type 0, color 5, and the group size is equal to groupSize[0] = 2.
	All elements have been removed, so the answer is true.



Example 2:


Input: types = [0,1,0], colors = [9,9,9], groupSize = [3,2]

Output: false

Explanation:


	No valid operation can be performed because no consecutive group satisfies its required size.
	Therefore, it is impossible to remove all elements, so the answer is false.



Example 3:


Input: types = [2,0,1,2], colors = [7,5,4,7], groupSize = [3,1,2]

Output: false

Explanation:​​​​​​​


	Remove the element at index 2. It has type 1, color 4, and forms a consecutive group of size groupSize[1] = 1.
	The remaining sequence is: types = [2, 0, 2], colors = [7, 5, 7].
	No further operations can be performed, so the answer is false.



 
Constraints:


	1 <= n == types.length == colors.length <= 105
	1 <= m == groupSize.length <= 105
	0 <= types[i] <= m - 1
	1 <= colors[i] <= 105
	1 <= groupSize[t] <= n

