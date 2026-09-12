class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)

        # There is exactly one way to make sum 0:
        # choose nothing.
        dp[0] = 1

        for total in range(1, target + 1):
            for num in nums:
                if total >= num:
                    dp[total] += dp[total - num]

        return dp[target]