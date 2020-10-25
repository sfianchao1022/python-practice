class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry_bit = 1
        rev_digits = reversed(digits)
        new_digits = []
        for item in rev_digits:
            item += carry_bit
            if item > 9:
                item -= 10
                new_digits.append(item)
            else:
                new_digits.append(item)
                carry_bit = 0

        if carry_bit == 1:
            new_digits.append(carry_bit)

        print(new_digits)

        return reversed(new_digits)


sol = Solution()
res = sol.plusOne([9, 5, 9])
ans = ""
for i in res:
    ans += str(i)

print(f"The array represents the integer {ans}.")

