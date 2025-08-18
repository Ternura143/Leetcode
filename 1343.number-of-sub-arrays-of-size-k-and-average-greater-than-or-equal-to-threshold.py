#
# @lc app=leetcode.cn id=1343 lang=python3
# @lcpr version=30204
#
# [1343] 大小为 K 且平均值大于等于阈值的子数组数目
#
# https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
#
# algorithms
# Medium (71.27%)
# Likes:    101
# Dislikes: 0
# Total Accepted:    58.3K
# Total Submissions: 81.8K
# Testcase Example:  '[2,2,2,2,5,5,5,8]\n3\n4'
#
# 给你一个整数数组 arr 和两个整数 k 和 threshold 。
# 
# 请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# 输出：3
# 解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4
# （threshold 的值)。
# 
# 
# 示例 2：
# 
# 输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# 输出：6
# 解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^4
# 1 <= k <= arr.length
# 0 <= threshold <= 10^4
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = i = sum = 0
        for j,x in enumerate(arr):
            sum += x
            if j < k - 1:
                continue
            if sum / k >= threshold:
                ans += 1
            sum -= arr[i]
            i += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [2,2,2,2,5,5,5,8]\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [11,13,17,23,29,31,7,5,2,3]\n3\n5\n
# @lcpr case=end

#

