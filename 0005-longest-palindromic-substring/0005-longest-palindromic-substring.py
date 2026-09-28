class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s

        start = 0
        max_len = 1

        def expand_around_center(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # When the loop terminates, s[left+1 : right] is the valid palindrome
            length = right - left - 1
            return left + 1, length

        for i in range(len(s)):
            # Odd-length palindromes (single-character center)
            l1, len1 = expand_around_center(i, i)
            if len1 > max_len:
                start = l1
                max_len = len1

            # Even-length palindromes (two-character center)
            l2, len2 = expand_around_center(i, i + 1)
            if len2 > max_len:
                start = l2
                max_len = len2

        return s[start : start + max_len]