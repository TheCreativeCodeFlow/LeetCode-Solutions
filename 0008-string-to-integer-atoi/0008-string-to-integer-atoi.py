class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        n = len(s)
        i = 0

        # 1. Skip leading whitespace
        while i < n and s[i] == " ":
            i += 1

        if i == n:
            return 0

        # 2. Check for optional sign
        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        # 3. Read digits and handle overflow
        res = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")

            # Check overflow before multiplying/adding
            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            res = res * 10 + digit
            i += 1

        return sign * res