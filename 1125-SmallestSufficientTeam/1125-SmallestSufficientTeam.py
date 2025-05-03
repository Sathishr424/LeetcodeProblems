# Last updated: 3/5/2025, 5:51:32 pm
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        skill_index = {skill: i for i, skill in enumerate(req_skills)}
        m = len(req_skills)
        full_mask = (1 << m) - 1

        # Convert each person's skills to a bitmask
        people_masks = []
        for person in people:
            mask = 0
            for skill in person:
                if skill in skill_index:
                    mask |= 1 << skill_index[skill]
            people_masks.append(mask)

        memo = {}
        best_team = list(range(n))  # worst case: everyone

        def dfs(mask, team):
            nonlocal best_team
            if mask == full_mask:
                if len(team) < len(best_team):
                    best_team = team[:]
                return

            if mask in memo and len(memo[mask]) <= len(team):
                return
            memo[mask] = team[:]

            for i in range(n):
                new_mask = mask | people_masks[i]
                if new_mask != mask:  # this person adds new skill(s)
                    dfs(new_mask, team + [i])

        dfs(0, [])
        return best_team
