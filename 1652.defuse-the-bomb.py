#
# @lc app=leetcode.cn id=1652 lang=python3
# @lcpr version=30204
#
# [1652] 拆炸弹
#
# https://leetcode.cn/problems/defuse-the-bomb/description/
#
# algorithms
# Easy (71.45%)
# Likes:    203
# Dislikes: 0
# Total Accepted:    75.6K
# Total Submissions: 105.8K
# Testcase Example:  '[5,7,1,4]\n3'
#
# 你有一个炸弹需要拆除，时间紧迫！你的情报员会给你一个长度为 n 的 循环 数组 code 以及一个密钥 k 。
# 
# 为了获得正确的密码，你需要替换掉每一个数字。所有数字会 同时 被替换。
# 
# 
# 如果 k > 0 ，将第 i 个数字用 接下来 k 个数字之和替换。
# 如果 k < 0 ，将第 i 个数字用 之前 k 个数字之和替换。
# 如果 k == 0 ，将第 i 个数字用 0 替换。
# 
# 
# 由于 code 是循环的， code[n-1] 下一个元素是 code[0] ，且 code[0] 前一个元素是 code[n-1] 。
# 
# 给你 循环 数组 code 和整数密钥 k ，请你返回解密后的结果来拆除炸弹！
# 
# 
# 
# 示例 1：
# 
# 输入：code = [5,7,1,4], k = 3
# 输出：[12,10,16,13]
# 解释：每个数字都被接下来 3 个数字之和替换。解密后的密码为 [7+1+4, 1+4+5, 4+5+7, 5+7+1]。注意到数组是循环连接的。
# 
# 
# 示例 2：
# 
# 输入：code = [1,2,3,4], k = 0
# 输出：[0,0,0,0]
# 解释：当 k 为 0 时，所有数字都被 0 替换。
# 
# 
# 示例 3：
# 
# 输入：code = [2,4,9,3], k = -2
# 输出：[12,5,6,13]
# 解释：解密后的密码为 [3+9, 2+3, 4+2, 9+4] 。注意到数组是循环连接的。如果 k 是负数，那么和为 之前 的数字。
# 
# 
# 
# 
# 提示：
# 
# 
# n == code.length
# 1 <= n <= 100
# 1 <= code[i] <= 100
# -(n - 1) <= k <= n - 1
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # 注释里是自己写的垃圾，这个题可以搞懂滑动窗口，取模模拟循环数组
        # n = len(code)
        # ans = n*[0]
        # sum1 = sum2 = 0
        # if k == 0:
        #     return ans

        # for i in range(n,2*n+k-1):
        #     sum1 += code[i%n]
        #     sum2 += code[(n+3*k+1)%n]
        #     if i<n+k-1:
        #         continue
        #     if k < 0:
        #         ans[i%n] = sum1
        #         sum1 -= code[(i-k+1)%n]
        #     if k > 0:
        #         ans[i%n] = sum2
        #         sum2 -= code[(i+1)%n]
        # return ans
        
        n = len(code)
        s = 0
        ans = n*[0]
        r = k+1 if k > 0 else n
        k = abs(k)
        s = sum(code[r-k:r])
        ans[0] = s
        for i in range(1,n):
            s += code[r%n] - code[(r-k)%n]
            ans[i] = s
            r+=1
        return ans
# @lc code=end



#
# @lcpr case=start
# [5,7,1,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,4,9,3]\n-2\n
# @lcpr case=end

#

