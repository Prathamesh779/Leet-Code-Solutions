class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in grid: row.sort()
        return sum(max(col)for col in zip(*grid))