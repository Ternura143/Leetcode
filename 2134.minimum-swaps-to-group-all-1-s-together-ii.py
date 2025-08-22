#
# @lc app=leetcode.cn id=2134 lang=python3
# @lcpr version=30204
#
# [2134] 最少交换次数来组合所有的 1 II
#
# https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together-ii/description/
#
# algorithms
# Medium (57.80%)
# Likes:    117
# Dislikes: 0
# Total Accepted:    24.7K
# Total Submissions: 42.7K
# Testcase Example:  '[0,1,0,1,1,0,0]'
#
# 交换 定义为选中一个数组中的两个 互不相同 的位置并交换二者的值。
# 
# 环形 数组是一个数组，可以认为 第一个 元素和 最后一个 元素 相邻 。
# 
# 给你一个 二进制环形 数组 nums ，返回在 任意位置 将数组中的所有 1 聚集在一起需要的最少交换次数。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [0,1,0,1,1,0,0]
# 输出：1
# 解释：这里列出一些能够将所有 1 聚集在一起的方案：
# [0,0,1,1,1,0,0] 交换 1 次。
# [0,1,1,1,0,0,0] 交换 1 次。
# [1,1,0,0,0,0,1] 交换 2 次（利用数组的环形特性）。
# 无法在交换 0 次的情况下将数组中的所有 1 聚集在一起。
# 因此，需要的最少交换次数为 1 。
# 
# 
# 示例 2：
# 
# 输入：nums = [0,1,1,1,0,0,1,1,0]
# 输出：2
# 解释：这里列出一些能够将所有 1 聚集在一起的方案：
# [1,1,1,0,0,0,0,1,1] 交换 2 次（利用数组的环形特性）。
# [1,1,1,1,1,0,0,0,0] 交换 2 次。
# 无法在交换 0 次或 1 次的情况下将数组中的所有 1 聚集在一起。
# 因此，需要的最少交换次数为 2 。
# 
# 
# 示例 3：
# 
# 输入：nums = [1,1,0,0,1]
# 输出：0
# 解释：得益于数组的环形特性，所有的 1 已经聚集在一起。
# 因此，需要的最少交换次数为 0 。
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] 为 0 或者 1
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # 感觉可以创建窗口，大小为k(k = num of 1's)，然后这样可以看窗口里取到最大1的数量，窗口减去就是交换次数
        # k = nums.count(1)
        # sum = ans = 0
        # for i,x in enumerate(nums):
        #     if x == 1:
        #         sum += 1
        #     if i < k-1:
        #         continue
        #     ans = max(ans, sum)
        #     if nums[i-k+1] == 1:
        #         sum -= 1
        # return k - ans
        n = len(nums)
        k = sum(nums)
        s = ans = 0
        for i in range(0,n+k-1):
            s += nums[i%n]
            if i < k-1:
                continue
            ans =max(ans,s)
            if nums[i-k+1] == 1:
                s -= 1
        return k -ans
        
# @lc code=end



#
# @lcpr case=start
# [0,1,0,1,1,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1,0,0,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,0,0,1]\n
# @lcpr case=end

#

