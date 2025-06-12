# Last updated: 12/6/2025, 5:43:40 am
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")