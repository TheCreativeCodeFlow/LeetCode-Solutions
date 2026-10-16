class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Mask with 32-bit integer mask to handle two's complement for negative numbers
        num &= 0xffffffff
        
        hex_chars = "0123456789abcdef"
        result = []
        
        while num > 0:
            # Extract lowest 4 bits
            digit = num & 0xf
            result.append(hex_chars[digit])
            # Shift right by 4 bits
            num >>= 4
            
        return "".join(reversed(result))