class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        rowdic = {}
        coldic = {}
        for i in range(len(grid)):
            col = tuple([row[i] for row in grid])
            row = tuple(grid[i])
            colval = coldic.get(col, 0)
            rowval = rowdic.get(row, 0)
            coldic[col] = colval + 1
            rowdic[row] = rowval + 1
        for i in rowdic:
            colval = coldic.get(i, 0)
            count += colval*rowdic[i]
             
        return count