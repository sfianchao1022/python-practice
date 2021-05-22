from typing import List  # list的泛型(Generic)版本


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = []
        for num in nums:
            if num not in temp:
                temp.append(num)
            else:
                temp.remove(num)
        print(temp)
        return temp[0]

    def hash_table(self, nums: List[int]):
        dict = {}  # dictionary
        for num in nums:
            dict[num] = dict.get(num, 0) + 1  # get value of num or default 0
        print(dict)

        for num in nums:
            if dict[num] == 1:
                return num

        return 0


sol = Solution()
print(f"ans : {sol.singleNumber([2, 1, 2, 1, 4, 3, 4])}")
print(f"ans : {sol.hash_table([3, 1, 3, 4, 4, 5, 1, 2, 2])}")

