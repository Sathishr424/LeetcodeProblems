# Last updated: 9/8/2025, 7:53:58 pm
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        
        # This function generates all subsets of the coin list (except the empty set),
        # and computes the LCM of each subset. It separates LCMs based on whether
        # the subset size is odd or even (for use in inclusion-exclusion principle).
        def computeLCM(arr):
            n = len(arr)
            oddLCM, evenLCM = [], []
            powerSet = 1 << n  # total 2^n subsets

            for mask in range(1, powerSet):  # exclude the empty subset
                bitCount = 0
                for j in range(n):
                    if mask & (1 << j):
                        bitCount += 1
                        if bitCount == 1:
                            lcm = arr[j]
                        else:
                            lcm = math.lcm(lcm, arr[j])  # compute LCM incrementally

                # Classify the LCM by parity of the subset size
                if bitCount % 2:
                    oddLCM.append(lcm)   # subsets with odd number of elements
                else:
                    evenLCM.append(lcm)  # subsets with even number of elements

            return (oddLCM, evenLCM)

        # This function applies the Inclusion-Exclusion Principle to count how many
        # numbers from 1 to m are divisible by at least one coin in the input set.
        def countIEP(oddLCM, evenLCM, m):
            odd, even = 0, 0
            for lcm in oddLCM:
                odd += m // lcm
            for lcm in evenLCM:
                even += m // lcm
            return odd - even  # total count of numbers divisible by at least one coin

        n = len(coins)
        nums = []

        # Remove coins that are multiples of other coins, as they are redundant
        for i in range(n):
            check = True
            for j in range(n):
                if i == j:
                    continue
                if coins[i] % coins[j] == 0:
                    check = False
                    break
            if check:
                nums.append(coins[i])  # keep only irreducible coins

        # Precompute LCMs needed for inclusion-exclusion
        oddLCM, evenLCM = computeLCM(nums)

        # Binary search for the smallest number m such that
        # there are exactly k numbers <= m divisible by at least one coin
        l, r = min(nums), k * max(nums)
        minV = r  # initialize with a large value

        while l <= r:
            m = (l + r) // 2
            kx = countIEP(oddLCM, evenLCM, m)

            if kx < k:
                l = m + 1  # need more divisible numbers
            elif kx > k:
                r = m - 1  # too many divisible numbers
            else:
                # Found a candidate, try to find a smaller one
                minV = min(minV, m)
                r = m - 1

        return minV  # the k-th smallest number divisible by any coin
