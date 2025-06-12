# Last updated: 12/6/2025, 5:44:31 am
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hash = defaultdict(int)
        for char in words[0]:
            hash[char] += 1
        
        for i in range(1, len(words)):
            new_hash = defaultdict(int)
            for char in words[i]:
                if char in hash and new_hash[char] < hash[char]:
                    new_hash[char] += 1
            hash = new_hash

        ret = []
        for k in new_hash:
            for _ in range(new_hash[k]):
                ret.append(k)
        
        return ret