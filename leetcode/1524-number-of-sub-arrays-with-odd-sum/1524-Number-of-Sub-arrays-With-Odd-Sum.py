class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7

        even = 1  # empty prefix sum (0)
        odd = 0
        prefix_sum = 0
        ans = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                ans = (ans + odd) % MOD
                even += 1
            else:
                ans = (ans + even) % MOD
                odd += 1

        return ans