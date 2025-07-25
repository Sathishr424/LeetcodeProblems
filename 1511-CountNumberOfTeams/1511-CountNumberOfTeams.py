# Last updated: 12/6/2025, 5:41:54 am
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        #TODO
        n = len(rating)
        teams = 0

        # Iterate through each soldier as the middle soldier
        for mid in range(n):
            left_smaller = 0
            right_larger = 0

            # Count soldiers with smaller ratings on the left side of the current soldier
            for left in range(mid - 1, -1, -1):
                if rating[left] < rating[mid]:
                    left_smaller += 1

            # Count soldiers with larger ratings on the right side of the current soldier
            for right in range(mid + 1, n):
                if rating[right] > rating[mid]:
                    right_larger += 1

            # Calculate and add the number of ascending rating teams (small-mid-large)
            teams += left_smaller * right_larger

            # Calculate soldiers with larger ratings on the left and smaller ratings on the right
            left_larger = mid - left_smaller
            right_smaller = n - mid - 1 - right_larger

            # Calculate and add the number of descending rating teams (large-mid-small)
            teams += left_larger * right_smaller

        # Return the total number of valid teams
        return teams