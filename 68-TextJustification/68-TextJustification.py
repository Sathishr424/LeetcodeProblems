# Last updated: 12/6/2025, 5:54:03 am
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words_arr = []
        len_arr = []

        curr_l = len(words[0])
        curr_word = [words[0]]
        for i in range(1, len(words)):
            if curr_l + len(words[i]) + 1 <= maxWidth:
                curr_l += len(words[i]) + 1
                curr_word.append(words[i])
            else:
                len_arr.append(curr_l)
                words_arr.append(curr_word)
                curr_l = len(words[i])
                curr_word = [words[i]]
        if curr_l:
            len_arr.append(curr_l)
            words_arr.append(curr_word)
        
        ret = []

        for i in range(len(words_arr)):
            curr_word = words_arr[i]
            curr_l = len_arr[i]

            rem = maxWidth - (curr_l - len(words_arr[i]) + 1)
            if i == len(words_arr)-1:
                curr = curr_word[0]
                for j in range(1, len(curr_word)):
                    curr += ' ' + curr_word[j]
                    rem -= 1
                curr += ' ' * rem
                ret.append(curr)
            else:
                curr = ''
                if len(curr_word) > 1:
                    gap = rem // (len(curr_word) - 1)
                    tmp = rem % (len(curr_word) - 1)
                    curr = curr_word[0] + ( ' ' * (gap + (tmp > 0)) )
                    tmp -= 1

                    for j in range(1, len(curr_word)-1):
                        curr += curr_word[j] + ( ' ' * (gap + (tmp > 0)) )
                        tmp -= 1
                    curr += curr_word[-1]
                else:
                    curr += curr_word[0] + (' ' * rem)
                ret.append(curr)
        return ret
                