# Last updated: 27/9/2025, 2:31:52 am
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creator_views = defaultdict(int)
        creator_popular = defaultdict(list)
        n = len(creators)
        max_views = 0
        for i in range(n):
            creator = creators[i]
            id = ids[i]
            view = views[i]
            creator_views[creator] += view
            max_views = max(max_views, creator_views[creator])
            creator_popular[creator].append((view, id))

        ret = []
        
        for creator in creator_views:
            if creator_views[creator] == max_views:
                creator_popular[creator].sort(key=lambda x: (-x[0], x[1]))
                ret.append( [ creator, creator_popular[creator][0][1] ] )

        return ret
            