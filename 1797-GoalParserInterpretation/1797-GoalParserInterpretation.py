# Last updated: 12/6/2025, 5:40:19 am
class Solution:
    def interpret(self, command: str) -> str:
        ret = ""
        i=0
        while i < len(command):
            if command[i] == 'G':
                ret += 'G'
            elif command[i] == '(' and command[i+1] == ')':
                ret += 'o'
                i+=1
            elif command[i] == '(' and command[i+1] == 'a':
                ret += 'al'
                i+=3
            i+=1
        return ret
                