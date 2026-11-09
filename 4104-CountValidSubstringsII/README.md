You are given a string s consisting only of the characters 'a', 'b', and 'c'.

A string is called valid if it does not contain "abc" as a subsequence.

Return the number of valid substrings in s. Substrings with different starting or ending indices are counted separately.

A substring is a contiguous non-empty sequence of characters within a string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 
Example 1:


Input: s = "abac"

Output: 9

Explanation:

The following substrings don't contain "abc"​​​​​​​ as a subsequence:


	s[0..0] = "a"
	s[0..1] = "ab"
	s[0..2] = "aba"
	s[1..1] = "b"
	s[1..2] = "ba"
	s[1..3] = "bac"
	s[2..2] = "a"
	s[2..3] = "ac"
	s[3..3] = "c"


Thus, the answer is 9.


Example 2:


Input: s = "abc"

Output: 5

Explanation:

The following substrings don't contain "abc"​​​​​​​ as a subsequence:


	s[0..0] = "a"
	s[0..1] = "ab"
	s[1..1] = "b"
	s[1..2] = "bc"
	s[2..2] = "c"​​​​​​​


Thus, the answer is 5.


Example 3:


Input: s = "ac"

Output: 3

Explanation:

All substrings in s don't contain "abc"​​​​​​​ as a subsequence. Thus, the answer is 3.


 
Constraints:


	1 <= s.length <= 105​​​​​​​
	s only consists of 'a', 'b', and 'c' characters.

