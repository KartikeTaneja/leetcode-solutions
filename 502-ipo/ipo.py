import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        """Maximize capital by selecting at most k projects greedily."""
        projects = sorted(zip(capital, profits))
        max_heap = []
        idx = 0
        
        for _ in range(k):
            while idx < len(projects) and projects[idx][0] <= w:
                heapq.heappush(max_heap, -projects[idx][1])
                idx += 1
            
            if not max_heap:
                break
            
            w += -heapq.heappop(max_heap)
        
        return w


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))  # 4
    print(sol.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))  # 6
    print(sol.findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 2]))  # 0
    print(sol.findMaximizedCapital(10, 0, [1, 2, 3], [0, 1, 1])) # 4