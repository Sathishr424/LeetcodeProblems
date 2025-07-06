# Last updated: 6/7/2025, 6:16:25 am
class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        nums1.sort()
        self.nums1 = nums1
        self.nums2 = nums2

        self.nums2_dict = defaultdict(int)
        for num in nums2:
            self.nums2_dict[num] += 1

    def add(self, index: int, val: int) -> None:
        self.nums2_dict[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.nums2_dict[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ret = 0
        for num in self.nums1:
            if num >= tot: break
            ret += self.nums2_dict[tot - num]
        
        return ret


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)