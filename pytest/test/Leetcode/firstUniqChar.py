"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # import pdb; pdb.set_trace()
        dic = {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                dic[s[i]] = -1

        print(dic)

        result = [x for x in dic.values() if x != -1]
        return min(result) if result else -1


S = Solution()
s = "leeottlccodde"
print('结果', S.firstUniqChar(s))


# 评价  难度3颗星  将s[i]作为字典的键非常巧妙，便于下一步有重复就可以用-1覆盖
