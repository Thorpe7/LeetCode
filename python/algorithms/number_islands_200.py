""" Script for number of islands 200 question"""

from typing import List

test_val1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]

test_val2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

class SolutionDFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid,i,j)
                    num_islands+=1
        return num_islands

    def dfs(self, grid:List[List[str]],r:int, c: int) -> None:

        if (
            r < 0
            or c < 0
            or r >= (len(grid))
            or c >= (len(grid[0]))
            or grid[r][c] != "1"
        ):
            return

        grid[r][c] = "0"
        # Now spread out and check around point
        self.dfs(grid, r-1, c)  # Check left cell
        self.dfs(grid, r+1, c)  # Check right cell
        self.dfs(grid, r, c-1)  # Check below
        self.dfs(grid, r, c+1)  # Check above


class SolutionBFS:
    pass




class SolutionUnionFind:
    pass








if __name__ == "__main__":
    sol = SolutionDFS()
    num_islands = sol.numIslands(grid=test_val1)
    print(f"Number of Islands found: {num_islands}")
    num_islands2 = sol.numIslands(grid=test_val2)
    print(f"Number of Islands found: {num_islands2}")