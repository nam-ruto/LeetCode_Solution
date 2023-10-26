def checkSymbol(char):
    if char == 'I':
        return 1

    elif char == 'V':
        return 5

    elif char == 'X':
        return 10

    elif char == 'L':
        return 50

    elif char == 'C':
        return 100
    
    elif char == 'D':
        return 500
    
    elif char == 'M':
        return 1000
    
def subtract(s, i):
    return checkSymbol(s[i+1]) - checkSymbol(s[i])

def checkSpecial(s, i):
    if(i == len(s)-1):
        return False
    elif((s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X')) or (s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C')) or (s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'))):
        return True

class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        res = 0
        i = 0
        while(i < n):
            if checkSpecial(s, i):
                res = res  + subtract(s, i)
                i += 2
            else:
                res = res + checkSymbol(s[i])
                i += 1
        return res

n = input()
s = Solution()
print(s.romanToInt(n))
        