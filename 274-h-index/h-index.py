class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """Find h-index: max h where researcher has >= h papers with >= h citations."""
        citations.sort(reverse=True)
        
        for i, cite in enumerate(citations):
            if cite < i + 1:
                return i
        
        return len(citations)


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.hIndex([3, 0, 6, 1, 5]))  # 3
    print(sol.hIndex([1, 3, 1]))        # 1
    print(sol.hIndex([100]))            # 1
    print(sol.hIndex([0, 0]))           # 0
    print(sol.hIndex([25, 8, 5, 3, 3])) # 3