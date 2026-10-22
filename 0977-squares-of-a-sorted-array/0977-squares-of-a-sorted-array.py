class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]

            if left_sq > right_sq:
                res[pos] = left_sq
                left += 1
            else:
                res[pos] = right_sq
                right -= 1
            pos -= 1

        return res