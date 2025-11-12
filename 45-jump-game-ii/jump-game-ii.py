class Solution:
    def jump(self, nums: list[int]) -> int:
        """Optimized: minimum jumps to reach last index."""
        jumps = currentEnd = farthest = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == currentEnd:
                jumps += 1
                currentEnd = farthest
        
        return jumps


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.jump([2, 3, 1, 1, 4]))  # 2
    print(sol.jump([2, 3, 0, 1, 4]))  # 2
    print(sol.jump([0]))               # 0
    print(sol.jump([5, 1, 1, 1, 1]))  # 1
    print(sol.jump([1, 1, 1, 0]))     # 3