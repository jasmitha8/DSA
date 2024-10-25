class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def isAlphaNumeric(c):
            if ord(c) in range(97, 97+26) or \
            ord(c) in range(65, 65+26) or \
            ord(c) in range(48, 58):
                return True
            return False

        while l <= r:
            if not isAlphaNumeric(s[l]):
                l += 1
                continue
            if not isAlphaNumeric(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome("A man, a plan, a canal: Panama"))
    