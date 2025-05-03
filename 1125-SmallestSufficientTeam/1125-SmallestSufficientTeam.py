# Last updated: 3/5/2025, 6:20:27 pm
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)

        skills_map = {}
        index = 0
        for skill in req_skills:
            skills_map[skill] = index
            index += 1
        
        people_skills = []
        for i in range(n):
            mask = 0
            for skill in people[i]:
                mask |= 1 << skills_map[skill]
            people_skills.append(mask)

        m = index
        start_mask = 1 << m
        full_mask = (1 << (m+1)) - 1

        dp = [[i for i in range(n)] for _ in range(full_mask + 1)]
        dp[start_mask] = []

        for mask in range(start_mask, full_mask):
            for i in range(n):
                new_mask = mask | people_skills[i]
                if new_mask != mask:
                    if len(dp[mask]) + 1 < len(dp[new_mask]):
                        dp[new_mask] = dp[mask] + [i]
        # print(dp)
        return dp[full_mask]