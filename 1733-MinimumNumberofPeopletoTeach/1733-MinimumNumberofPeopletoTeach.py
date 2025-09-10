# Last updated: 10/9/2025, 4:51:27 pm
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:   
        users_know = defaultdict(dict)
        
        for i in range(len(languages)):
            for l in languages[i]:
                users_know[i + 1][l] = 1
        
        need_to_teach = []
        for u, v in friendships:
            for l in languages[u-1]:
                if l in users_know[v]:
                    break
            else:
                need_to_teach.append((u, v))

        def count(l):
            extra = defaultdict(dict)
            ans = 0
            for u, v in need_to_teach:
                u_there = l in users_know[u] or l in extra[u]
                v_there = l in users_know[v] or l in extra[v]
                
                if not u_there:
                    ans += 1
                    extra[u][l] = 1
                if not v_there:
                    ans += 1
                    extra[v][l] = 1
            
            return ans
        
        min_count = inf
        for l in range(1, n + 1):
            min_count = min(min_count, count(l))
        
        return min_count
            
