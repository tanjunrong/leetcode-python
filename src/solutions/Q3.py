class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_number = 0
        number = 0
        sub = ""
        for i in s:
            if i in sub:
                max_number = max(number, max_number)
                number -= sub.index(i)
                sub = sub[(sub.index(i) + 1):]
            else:
                number += 1
            sub += i
        return max(max_number, number)



