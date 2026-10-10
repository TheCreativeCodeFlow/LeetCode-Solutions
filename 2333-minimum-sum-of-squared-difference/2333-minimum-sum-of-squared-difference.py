class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        
        # If total modifications exceed total absolute difference, we can reduce all differences to 0
        if sum(diffs) <= k:
            return 0
        
        max_diff = max(diffs)
        count = [0] * (max_diff + 1)
        for d in diffs:
            count[d] += 1
            
        # Greedily reduce the highest differences downward
        for d in range(max_diff, 0, -1):
            if count[d] == 0:
                continue
            
            if k >= count[d]:
                k -= count[d]
                count[d - 1] += count[d]
                count[d] = 0
            else:
                count[d - 1] += k
                count[d] -= k
                k = 0
                break
                
        return sum(d * d * cnt for d, cnt in enumerate(count))