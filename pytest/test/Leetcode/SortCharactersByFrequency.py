'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


'''


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        li = list(s)
        li.sort()
        dic = {}
        for i in range(len(li)):
            dic[li[i]] = 1


        for i in range(len(li)):
            if i+1 < len(li) and li[i]==li[i+1]:
                dic[li[i]] += 1
        print(dic)

        # sort dictionary by values and reverse
        sorted_by_value = sorted(dic.items(), key=lambda kv: kv[1], reverse=True)
        print(sorted_by_value)
        res = [i[0]*i[1] for i in sorted_by_value]
        result = ''
        for i in res:
            result = result + i

        print(result)
        return result


S = Solution()
s = 'sjdkhafslasjkdfNSGAJjsc'
S.frequencySort(s)


'''
sorted_by_value = sorted(dic.items(), key=lambda kv: kv[1], reverse=True)
Brillent 
'''
