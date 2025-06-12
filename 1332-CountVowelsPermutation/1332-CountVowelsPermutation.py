# Last updated: 12/6/2025, 5:42:52 am
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = (10**9) + 7
        memo = {'a': ['e'], 'e': ['a','i'], 'i': ['a','e','o','u'], 'o': ['i','u'], 'u': ['a']}
        hash =  {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

        for i in range(1, n):
            tmp = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
            for k in memo:
                for c in memo[k]:
                    tmp[c] += hash[k]
            hash = tmp
        cnt = 0
        for k in hash:
            cnt += hash[k]
        return cnt % mod

# a-> {e}         //Each vowel 'a' may only be followed by an 'e'. 
# e-> {a,i}       //Each vowel 'e' may only be followed by an 'a' or an 'i'.
# i-> {a,e,o,u}   //Each vowel 'i' may not be followed by another 'i'.
# o-> {i,u}       //Each vowel 'o' may only be followed by an 'i' or a 'u'.
# u-> {a}         //Each vowel 'u' may only be followed by an 'a'.