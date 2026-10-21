class Solution:
    def findComplement(self, num: int) -> int:
        # Create a mask with all 1s matching the bit length of num
        mask = (1 << num.bit_length()) - 1
        return num ^ mask