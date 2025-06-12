# Last updated: 12/6/2025, 5:54:13 am
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==0: return []
        if n==1: return [[1]]
        ret = [[0]*n for i in range(n)]
        x,y=0,0
        dir = 'r'
        for i in range(n*n):
            print(x,',',y,',',dir,',',i+1)
            ret[y][x] = i+1
            if dir == 'r':
                if x+1 >= n or ret[y][x+1] != 0:
                    dir = 'd'
                    y+=1
                    if y >= n: break
                else: x+=1
            elif dir == 'd':
                if y+1 >= n or ret[y+1][x] != 0:
                    dir = 'l'
                    x-=1
                    if x < 0: break
                else: y+=1
            elif dir == 'l':
                if x-1 < 0 or ret[y][x-1] != 0:
                    dir = 'u'
                    y-=1
                    if y < 0: break
                else: x-=1
            elif dir == 'u':
                if y-1 < 0 or ret[y-1][x] != 0:
                    dir = 'r'
                    x+=1
                    if x >= n: break
                else: y-=1
        return ret