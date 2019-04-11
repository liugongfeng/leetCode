class Solution:
    def minimumTotal(self, triangle):
        if not triangle:    return 0

        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        
        return res[0]


s = Solution()
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
res = s.minimumTotal(triangle)