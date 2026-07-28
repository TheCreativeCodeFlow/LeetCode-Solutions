class Solution:
    def smallestPalindrome(self, s: str) -> str:
        half = "".join(sorted(s[:len(s) // 2]))
        return half + (s[len(s) // 2] if len(s) % 2 else "") + half[::-1]