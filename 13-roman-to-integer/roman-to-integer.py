class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        res = 0
        prev = 0

        for ch in reversed(s):
            curr = roman[ch]
            if curr < prev:
                res -= curr
            else:
                res += curr
            prev = curr

        return res