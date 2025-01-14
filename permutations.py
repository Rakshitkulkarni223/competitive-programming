# Given an array nums of distinct integers, return all the possible 
# permutations
# . You can return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]

class Solution(object):
    def solve(self, arr, ans, res):
        if not arr:
            res.append(ans)
        
        for i in range(len(arr)):
            self.solve(arr[:i]+arr[i+1:], ans + [arr[i]], res)

    def permute(self, nums):
        res = []
        self.solve(sorted(nums), [], res)
        return res

c = Solution()
print(c.permute([1,2,3]))