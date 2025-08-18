#
# @lc app=leetcode.cn id=2841 lang=python3
# @lcpr version=30204
#
# [2841] 几乎唯一子数组的最大和
#
# https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/description/
#
# algorithms
# Medium (45.85%)
# Likes:    76
# Dislikes: 0
# Total Accepted:    32.8K
# Total Submissions: 71.5K
# Testcase Example:  '[2,6,7,3,1,7]\n3\n4'
#
# 给你一个整数数组 nums 和两个正整数 m 和 k 。
# 
# 请你返回 nums 中长度为 k 的 几乎唯一 子数组的 最大和 ，如果不存在几乎唯一子数组，请你返回 0 。
# 
# 如果 nums 的一个子数组有至少 m 个互不相同的元素，我们称它是 几乎唯一 子数组。
# 
# 子数组指的是一个数组中一段连续 非空 的元素序列。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [2,6,7,3,1,7], m = 3, k = 4
# 输出：18
# 解释：总共有 3 个长度为 k = 4 的几乎唯一子数组。分别为 [2, 6, 7, 3] ，[6, 7, 3, 1] 和 [7, 3, 1, 7]
# 。这些子数组中，和最大的是 [2, 6, 7, 3] ，和为 18 。
# 
# 
# 示例 2：
# 
# 输入：nums = [5,9,9,2,4,5,4], m = 1, k = 3
# 输出：23
# 解释：总共有 5 个长度为 k = 3 的几乎唯一子数组。分别为 [5, 9, 9] ，[9, 9, 2] ，[9, 2, 4] ，[2, 4, 5] 和
# [4, 5, 4] 。这些子数组中，和最大的是 [5, 9, 9] ，和为 23 。
# 
# 
# 示例 3：
# 
# 输入：nums = [1,2,1,2,1,2,1], m = 3, k = 3
# 输出：0
# 解释：输入数组中不存在长度为 k = 3 的子数组含有至少  m = 3 个互不相同元素的子数组。所以不存在几乎唯一子数组，最大和为 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 2 * 10^4
# 1 <= m <= k <= nums.length
# 1 <= nums[i] <= 10^9
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # ans = sum = 0
        # l = []
        # for i,x in enumerate(nums):
        #     l.append(x)
        #     sum += x
        #     if i < k-1:
        #         continue
        #     if len(set(l)) >= m:    
        #         ans = max(ans,sum)
        #     l.pop(0)
        #     sum -= nums[i-k+1]
        # return ans
        ans = s = 0
        cnt = defaultdict(int)
        for i,x in enumerate(nums):
            s += x
            cnt[x] += 1
            left = i-k+1
            if left < 0:
                continue

            if len(cnt) >= m:
                ans = max(ans, s)
            out = nums[left]
            s -= out
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]
        return ans
        
        
# @lc code=end



#
# @lcpr case=start
# [2,6,7,3,1,7]\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [5,9,9,2,4,5,4]\n1\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2,1,2,1]\n3\n3\n
# @lcpr case=end

#

