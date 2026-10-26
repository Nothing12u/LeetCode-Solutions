from collections import deque
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        divisible_islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    island_sum = grid[i][j]
                    grid[i][j] = 0  
                    queue = deque([(i, j)])

                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  
                                queue.append((nr, nc))

                    if island_sum % k == 0:
                        divisible_islands += 1

        return divisible_islands