class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            chars = {}
            for i in range(len(s)):
                if s[i] in chars:
                    chars[s[i]] = chars.get(s[i]) + 1
                else:
                    chars[s[i]] = 1
            print(chars)
            
            for i in range(len(t)):
                if t[i] in chars:
                    if chars[t[i]] == 1:
                        chars.pop(t[i])
                    else:
                        chars[t[i]] = chars.get(t[i]) - 1
                else: 
                    return False

            return len(chars) == 0
