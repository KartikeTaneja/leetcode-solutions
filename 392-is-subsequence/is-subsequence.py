class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Check if s is a subsequence of t using two pointers."""
        i = 0
        for char in t:
            if i < len(s) and char == s[i]:
                i += 1
        return i == len(s)


# For follow-up: preprocess t for multiple queries
class SubsequenceChecker:
    def __init__(self, t: str):
        """Preprocess t to store next occurrence of each character."""
        self.n = len(t)
        self.next = [[self.n] * 26 for _ in range(self.n + 1)]
        
        for i in range(self.n - 1, -1, -1):
            for c in range(26):
                self.next[i][c] = self.next[i + 1][c]
            self.next[i][ord(t[i]) - ord('a')] = i
    
    def isSubsequence(self, s: str) -> bool:
        """Check if s is subsequence of t in O(len(s)) time."""
        pos = 0
        for char in s:
            idx = ord(char) - ord('a')
            if self.next[pos][idx] == self.n:
                return False
            pos = self.next[pos][idx] + 1
        return True


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.isSubsequence("abc", "ahbgdc"))   # True
    print(sol.isSubsequence("axc", "ahbgdc"))   # False
    print(sol.isSubsequence("", "ahbgdc"))      # True
    print(sol.isSubsequence("abc", ""))         # False
    print(sol.isSubsequence("aaa", "aa"))       # False
    
    # Follow-up: multiple queries
    print("\nFollow-up test:")
    checker = SubsequenceChecker("ahbgdc")
    print(checker.isSubsequence("abc"))         # True
    print(checker.isSubsequence("axc"))         # False
    print(checker.isSubsequence("adc"))         # True