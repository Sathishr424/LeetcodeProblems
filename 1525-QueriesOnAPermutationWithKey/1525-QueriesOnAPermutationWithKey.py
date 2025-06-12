# Last updated: 12/6/2025, 5:41:50 am
class Solution:
    def processQueries(self, queries, m):
        ret = []
        p = [i for i in range(1,m+1)]
        for i in range(len(queries)):
            index = p.index(queries[i])
            ret.append(index)
            p.insert(0,p[index])
            del p[index+1]
        return ret