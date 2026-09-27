class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to guarantee O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        low, high = 0, m

        while low <= high:
            i = (low + high) // 2  # Partition point in nums1
            j = half - i           # Partition point in nums2

            # Left and right boundary values around partitions
            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")

            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            # Check if partition is valid
            if left1 <= right2 and left2 <= right1:
                # Odd total length: median is max of the left partition
                if total % 2 != 0:
                    return float(max(left1, left2))
                # Even total length: average of the two middle elements
                return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                # Too far right in nums1, search left
                high = i - 1
            else:
                # Too far left in nums1, search right
                low = i + 1

        return 0.0