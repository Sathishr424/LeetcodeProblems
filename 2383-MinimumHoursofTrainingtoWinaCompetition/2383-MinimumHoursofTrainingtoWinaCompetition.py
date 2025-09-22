# Last updated: 22/9/2025, 10:31:47 pm
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        n = len(experience)

        hours = 0
        for i in range(n):
            e = energy[i]
            exp = experience[i]

            if initialEnergy <= e:
                diff = e - initialEnergy + 1
                initialEnergy += diff
                hours += diff

            if initialExperience <= exp:
                diff = exp - initialExperience + 1
                initialExperience += diff
                hours += diff

            initialExperience += exp
            initialEnergy -= e

        return hours
            
                