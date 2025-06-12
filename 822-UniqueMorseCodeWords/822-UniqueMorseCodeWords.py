# Last updated: 12/6/2025, 5:46:25 am
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alp = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        hash = {}
        for word in words:
            s = ""
            for c in word:
                s += alp[ord(c)-97]
            if s not in hash: hash[s] = 1
        return len(hash)
