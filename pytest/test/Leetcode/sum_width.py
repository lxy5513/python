"""
Given an array of integers A, consider all non-empty subsequences of A.

For any sequence S, let the width of S be the difference between the maximum and minimum element of S.

Return the sum of the widths of all subsequences of A.

As the answer may be very large, return the answer modulo 10^9 + 7.



Example 1:

Input: [2,1,3]
Output: 6
Explanation:
Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.


Note:

1 <= A.length <= 20000
1 <= A[i] <= 20000


import itertools

class Solution:
    def sumSubseqWidths(self, A):

        # :type A: List[int]
        # :rtype: int

        L = []
        for i in range(1, len(A)+1):
            item = itertools.combinations(A, i)
            # list add list
            L.extend(list(item))

        print(L)
        Sum = 0
        for i in L:
            min_ = min(i)
            max_ = max(i)
            item_len = max_ - min_
            Sum += item_len

        return Sum

S = Solution()
l = [21,12,8,21,11,35,36,10,30,29,28,1,24,23,36,30,38,17,14,37]
res = S.sumSubseqWidths(l)
print(res)
"""
'''
difficult points
1. how to 得到任意的排列组合在一个list中
    itertools.combinations(list, i)
2. list + list 
    list1.extend(list2)
3. 时间复杂度
    
'''

# 阶乘
def factorial(x):
  result = 1
  for i in range(2, x + 1):
    result *= i
  return result

def sum_fac(x):
    sum_ = 0
    for i in range(len(x)):
        sum_ += factorial(i)
    return sum_

import itertools
class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sum_ = 0
        while A != []:
            max_ = max(A)
            B = A[:]
            while B != []:
                min_ = min(B)
                sub_ = max_ - min_
                if len(B) > 2:
                    res = 2 + factorial(len(B)-2)
                else:
                    res = 1
                print('='*20, res*sub_)
                sum_ += res*sub_
                print('-'*20, B)
                B.remove(min_)
            A.remove(max_)
        return sum_

S = Solution()
l = [1,2,3,5,9]
res = S.sumSubseqWidths(l)
print(res)

# 未解决

