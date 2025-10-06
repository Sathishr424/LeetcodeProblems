# Last updated: 6/10/2025, 10:22:54 pm
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height
        bulky = volume >= 10**9 or max(length, width, height) >= 10 ** 4
        heavy = mass >= 100

        if bulky and heavy:
            return 'Both'
        elif bulky:
            return 'Bulky'
        elif heavy:
            return 'Heavy'
        else:
            return 'Neither'