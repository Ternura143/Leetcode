#
# @lc app=leetcode.cn id=219 lang=python3
# @lcpr version=30204
#
# [219] 存在重复元素 II
#
# https://leetcode.cn/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (49.99%)
# Likes:    815
# Dislikes: 0
# Total Accepted:    411.9K
# Total Submissions: 823K
# Testcase Example:  '[1,2,3,1]\n3'
#
# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i
# - j) <= k 。如果存在，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,3,1], k = 3
# 输出：true
# 
# 示例 2：
# 
# 输入：nums = [1,0,1,1], k = 1
# 输出：true
# 
# 示例 3：
# 
# 输入：nums = [1,2,3,1,2,3], k = 2
# 输出：false
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last = defaultdict(int)
        for i,x in enumerate(nums):
            if x in last and i - last[x] <= k:
                return True
            else:
                last[x] = i
        return False
                
                
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,2,3]\n2\n
# @lcpr case=end

#

