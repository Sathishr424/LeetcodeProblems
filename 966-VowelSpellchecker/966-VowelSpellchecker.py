# Last updated: 14/9/2025, 10:18:23 am
class Solution:
    def spellchecker(self, wordList: List[str], queries: List[str]) -> List[str]:
        n = len(wordList)
        
        words = set(wordList)
        v_words = {}
        c_words = {}

        for word in wordList:
            if word.lower() not in c_words:
                c_words[word.lower()] = word
            
            n_word = ''
            for char in word.lower():
                if char in 'aeiou':
                    n_word += '*'
                else:
                    n_word += char
            
            if n_word not in v_words:
                v_words[n_word] = word

        ret = []
        for word in queries:
            if word in words:
                ret.append(word)
            else:
                if word.lower() in c_words:
                    ret.append(c_words[word.lower()])
                    continue
                
                n_word = ''
                for char in word.lower():
                    if char in 'aeiou':
                        n_word += '*'
                    else:
                        n_word += char

                if n_word in v_words:
                    ret.append(v_words[n_word])
                else:
                    ret.append('')

        return ret