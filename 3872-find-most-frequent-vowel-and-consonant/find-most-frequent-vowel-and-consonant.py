class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts = [0] * 26
        for char in s:
            counts[ord(char) - 97] += 1
        vowel_indices = {0, 4, 8, 14, 20}
        max_vowel = 0
        max_consonant = 0
        for i in range(26):
            if counts[i] > 0:
                if i in vowel_indices:
                    if counts[i] > max_vowel:
                        max_vowel = counts[i]
                else:
                    if counts[i] > max_consonant:
                        max_consonant = counts[i]
        return max_vowel + max_consonant
