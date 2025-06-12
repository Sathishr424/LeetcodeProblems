# Last updated: 12/6/2025, 5:46:20 am
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hash = {}
        ban = {}
        for word in banned:
            ban[word] = 1
        st = ""

        for p in paragraph.lower():
            if ord(p) >= 97 and ord(p) <= 122:
                st += p
            else:
                st += ' '
        
        st = st.split(' ')

        ret = [0, ""]
        for word in st:
            if not word or word in ban: continue
            if word in hash: 
                hash[word] += 1
            else: hash[word] = 1
            if hash[word] > ret[0]:
                ret = [hash[word], word]
        
        return ret[1]