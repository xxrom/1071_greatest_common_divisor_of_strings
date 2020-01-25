class Solution:
    def check(self, str0: str, str1: str, checkStr: str) -> bool:
        '''
        Check checkStr string
        should be included correctly in str0 and str1

        Example:
          'abab' and 'ababab'
        the answer -> 'ab'
        not 'abab'!
        '''

        # Check situation if it's possible by number:
        # (str0 = checkStr * X) and (str1 = checkStr * Y)
        if (len(str0) % len(checkStr) == 0 and
            len(str1) % len(checkStr) == 0 and
            len(str0) // len(checkStr) > 0 and
                len(str1) // len(checkStr) > 0):

            # Check situation on practice:
            # (str0 = checkStr * X) and (str1 = checkStr * Y)
            if (str0 == checkStr * (len(str0) // len(checkStr)) and
                    str1 == checkStr * (len(str1) // len(checkStr))):
                return True
        return False

        '''
        # debug mode
        mod01 = len(s0) % len(s1)
        mod11 = len(str1) % len(s1)
        div01 = len(s0) // len(s1)
        div11 = len(str1) // len(s1)
        # print('01 mod %d, // %d' % (mod01, div01))
        # print('10 mod %d, // %d' % (mod11, div11))

        if mod01 == 0 and mod11 == 0 and div01 > 0 and div11 > 0:
            # print(s0)
            # print(s1 * div01)
            # print(str1)
            # print(s1*div11)
            if s0 == s1 * div01 and str1 == s1 * div11:
                return True
        return False
        '''

    def gcdOfStrings(self, str0: str, str1: str) -> str:
        print(str0, str1)

        checkStr = ''
        ansStr = ''

        for char in str1:
            checkStr += char
            isSame = self.check(str0, str1, checkStr)
            if isSame:
                ansStr = checkStr

        return ansStr


my = Solution()

ansStr = my.gcdOfStrings('abab', 'abababab')
# ansStr = my.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX",
#                          "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")
print('ansStr',  ansStr)

# TAUXXTAUXXTAUXXTAUXXTAUXX TAUXXTAUXXTAUXXTAUXXTAUXX  TAUXXTAUXXTAUXXTAUXX
# ansStr TAUXXTAUXXTAUXXTAUXXTAUXX

# Runtime: 48 ms, faster than 10.65% of Python3 online submissions for Greatest Common Divisor of Strings.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Greatest Common Divisor of Strings.
