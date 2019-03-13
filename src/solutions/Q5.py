# 1.暴力2.中心扩展3.马拉车算法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp = "#"
        for i in s:
            temp += i + "#"
        radius = [0] * len(temp)

        r = 0  # 最右回文边界
        c = 0  # 最右回文中心
        max_len = -1  # 最长回文长度
        max_index = -1  # 最长回文中心

        for i in range(len(temp)):
            radius[i] = min(radius[2 * c - i], r - i + 1)

            while i + radius[i] < len(temp) and i - radius[i] > -1:
                if temp[i - radius[i]] == temp[i + radius[i]]:
                    radius[i] += 1
                else:
                    break

            if i + radius[i] > r:
                r = i + radius[i] - 1
                c = i

            if radius[i] > max_len:
                max_len = radius[i]
                max_index = i
        return s[int((max_index - max_len) / 2 + 1):
                 int((max_index + max_len) / 2)]

