class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        letter_conversion = {"a" : "b", "b" : "c", "c" : "d", "d" : "e", "e" : "f", "f" : "g", "g" : "h", "h": "i", "i":"j", "j" : "k", "k" : "l", "l": "m", "m" : "n", "n" : "o", "o" : "p", "p" : "q", "q" : "r", "r" : "s", "s" : "t", "t" : "u", "u" : "v", "v" : "w", "w" : "x", "x" : "y", "y" : "z", "z" : "a"}
        temp_letter_track = 1

        while(temp_letter_track <= k):
            print(word)
            print(temp_letter_track)
            temp_append = ""
            temp_letter_track = len(word)
            for char in word:
                temp_append += letter_conversion[char]
            word += temp_append
           

        return word[k-1]