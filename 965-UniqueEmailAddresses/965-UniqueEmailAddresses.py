# Last updated: 12/6/2025, 5:45:14 am
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hash = {}

        for email in emails:
            local, domain = email.split('@')
            hash[re.sub("\+.*", '', local).replace('.', '') + "@" + domain] = 1

        return len(hash)

                
