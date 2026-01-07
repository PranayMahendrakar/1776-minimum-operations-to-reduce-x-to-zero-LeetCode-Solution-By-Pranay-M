class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # Equivalent to finding longest subarray with sum = total - x
        target = sum(nums) - x
        
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        
        # Sliding window to find longest subarray with sum = target
        n = len(nums)
        max_len = -1
        current_sum = 0
        left = 0
        
        for right in range(n):
            current_sum += nums[right]
            
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return n - max_len if max_len != -1 else -1