class Solution:
    def isValid(self, word: str) -> bool:
        vowel, consonant, other = False, False, False
        for char in word:
            if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowel = True
            elif char.isalpha():
                consonant = True
            elif char.isdigit():
                continue
            else:
                other = True
        return len(word) >= 3 and vowel and consonant and not other