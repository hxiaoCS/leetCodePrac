class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, left = 0, 0
        count = defaultdict(int)
        max_repeat = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_repeat = max(max_repeat, count[s[right]])

            while right - left + 1 - max_repeat > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res


