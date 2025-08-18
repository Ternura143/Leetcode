# Leetcode note

## 滑动窗口系列  

### 定长滑窗题目

灵神解题思路：
<https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/solutions/2809359/tao-lu-jiao-ni-jie-jue-ding-chang-hua-ch-fzfo>

定长滑窗套路
窗口右端点在 $i$ 时，由于窗口长度为 $k$，所以窗口左端点为 $i−k+1$。

总结成三步：入-更新-出。

入：下标为 $i$ 的元素进入窗口，更新相关统计量。如果窗口左端点 $i−k+1<0$，即 $i<k−1$，则尚未形成第一个窗口，重复第一步。
更新：更新答案。一般是更新最大值/最小值。
出：下标为 $i−k+1$ 的元素离开窗口，更新相关统计量，为下一个循环做准备。

example:1456

``` python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = vowel = 0
        for i, c in enumerate(s):
            # 1. 进入窗口
            if c in "aeiou":
                vowel += 1
            if i < k - 1:  # 窗口大小不足 k
                continue
            # 2. 更新答案
            ans = max(ans, vowel)
            # 3. 离开窗口，为下一个循环做准备
            if s[i - k + 1] in "aeiou":
                vowel -= 1
        return ans
```

在统计窗口内是否有重复元素，可以使用defaultdict。
比起使用List好处在于，defaultdict可以方便地统计元素出现的频次，而不需要手动维护一个List来记录元素的位置。
使用方式举例：（只是举例，对应题目可以参考2841）

``` python
from collections import defaultdict

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans = s = 0
        cnt = defaultdict(int)
        for i, x in enumerate(nums):
            # 1. 进入窗口
            s += x
            cnt[x] += 1
            left = i - k + 1
            if left < 0:  # 窗口大小不足 k
                continue
            # 2. 更新答案
            if len(cnt) >= m:
                ans = max(ans, s)
            # 3. 离开窗口
            out = nums[left]
            s -= out
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]
        return ans
```
