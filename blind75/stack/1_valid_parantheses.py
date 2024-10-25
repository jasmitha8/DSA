class Solution:
    def isValid(self, s: str) -> bool:
        bracketDict = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c not in bracketDict:
                stack.append(c)
            else:   # closing bracket in s
                if not stack:
                    return False
                bracket = stack.pop()
                if bracketDict[c] != bracket:
                    return False
        if stack:
            return False
        return True

if __name__ == "__main__":
    obj = Solution()
    print(obj.isValid("([])"))