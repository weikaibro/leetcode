class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""
        length = 0
        last_char = ""
        for char in num:
            if char == last_char:
                length += 1
                if length == 3 and char * 3 > result:
                    result = char * 3
            else:
                last_char = char
                length = 1
        return result