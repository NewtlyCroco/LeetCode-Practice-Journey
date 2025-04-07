class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        letter_conversion = {"a" : "b", "b" : "c", "c" : "d", "d" : "e", "e" : "f", "f" : "g", "g" : "h", "h": "i", "i":"j", "j" : "k", "k" : "l", "l": "m", "m" : "n", "n" : "o", "o" : "p", "p" : "q", "q" : "r", "r" : "s", "s" : "t", "t" : "u", "u" : "v", "v" : "w", "w" : "x", "x" : "y", "y" : "z", "z" : "a"}
        temp_letter_track = 1 #hashmap for the win, although in a new instane of this problem, I can just iterate over characters like using a+1 as in bits this will be equivilent to b

        while(temp_letter_track <= k):
            temp_append = ""
            temp_letter_track = len(word)#was having a problem here, but fixed it, as we need to change length before processing, so we execute one more additional time, just based on how I have formated this code!
            for char in word:#this is fulfulling the "At least k integers" part of the problem!
                temp_append += letter_conversion[char]
            word += temp_append
           

        return word[k-1]#this is because we are on zero index, so we need to look at the number before our final to get true value!