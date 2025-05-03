# Last updated: 3/5/2025, 5:47:12 pm
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)

        skills_map = {}
        index = 0
        for skill in req_skills:
            skills_map[skill] = index
            index += 1
        
        m = index
        start_mask = 1 << m
        full_mask = (1 << (m+1)) - 1
        visited = [0] * n

        ret = [i for i in range(n)]
        memo = [n] * (full_mask + 1)

        def rec(mask, team):
            nonlocal ret
            if mask == full_mask:
                if len(team) < len(ret):
                    ret = team + []
                return 0
            
            if memo[mask] <= len(team): return 0
            memo[mask] = len(team)

            for i in range(n):
                if visited[i] == 0:
                    
                    new_mask = mask
                    for skill in people[i]:
                        index = skills_map[skill]
                        if mask & (1 << index) == 0:
                            new_mask |= 1 << index
                    
                    if new_mask != mask:
                        visited[i] = 1
                        team.append(i)
                        rec(new_mask, team)
                        team.pop()
                        visited[i] = 0
            
            return 0

        rec(start_mask, [])
        return ret