class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left, right = 0, 0
        charset = set()

        while right < len(s):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1

            charset.add(s[right])
            res = max(res, len(charset))
            right += 1

        return res





        return res
                