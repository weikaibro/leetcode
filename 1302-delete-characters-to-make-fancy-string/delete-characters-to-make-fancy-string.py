class Solution:
    def makeFancyString(self, s: str) -> str:
        result = [s[0]]
        freq = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                freq += 1
            else:
                freq = 1
            if freq < 3:
                result.append(s[i])
        return "".join(result)