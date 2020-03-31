from collections import deque

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        # regex
        # get the first item store it in a list, get the second item check if it is the key or value of the first item
        stack = deque()
        print("stack", stack)
        # print("s", s)
        # lst = []
        valid = {'(':')', '[':']', '{':'}'}
        # if len(s) % 2 != 0:
        #     return False
        match_count = len(s)//2
        count = 0
        for i in range(len(s)):
            if s[i] in valid.keys():
                stack.append(s[i])
                print("stack", stack)
            else:
                print("count", count, match_count)
                if len(stack) == 0 and match_count != count:
                    return False
                if valid.get(stack.pop()) == s[i]:
                    print("balanced parenthesis")
                    count += 1
                # else:
                #     print("Not balanced")
                #     return False
                # print("pop", stack.pop())
                # print("getting")
                # print("getting", valid.get('k'))
        if match_count == count:
            return True
        return False


print(isValid("){"))

















# for p in s:
#     if (p in valid.keys() or p in valid.values()) and len(lst) == 0:
#         lst.append(p)
#     elif p in valid.keys() and len(lst) != 0 and valid[p] == lst[-1]:
#         lst.append(p)
#         print("Hi")
#         return True
#     elif p in valid.values() and len(lst) != 0 and valid.get(lst[-1]) == p:
#         # print
#         lst.append(p)
#         print("Hello")
#         return True
# return False



# def isValid(s: str) -> bool:
#         stack = []
#         d = {')': '(', '}': '{', ']': '['}
#         for c in s:
#             print(c)
#             if c in d.values():
#                 stack.append(c)
#             elif not stack or stack.pop() != d[c]:
#                 print("stack", stack)
#                 return False
#         print("stack", stack)
#         if not stack:
#             return True
#         else:
#             False

























        # sli = 1
        # index = 0
        # prefix = ''
        # if len(strs) == 1:
        #     return strs[0]
        # prefix = ''
        # pre = strs[index][0:sli]
        # for i in range(len(strs)):
        #     print("preeee", pre)
        #     for j in range(len(strs)):
        #         if pre == strs[j][0:sli] and len(strs)-1 == j:
        #             prefix = pre
        #             print(pre, strs[j][0:sli])
        #             print(len(strs)-1, j)
        #             print( pre == strs[j][0:sli] and len(strs)-1 == j)
        #             print("WHY")
        #             return prefix
        #         elif pre != strs[j][0:sli]:
        #             print("IN THE ")
        #             return prefix
        #         else:
        #             continue
        #     sli += 1
        #     index += 1
        #     print("pre", pre)
        #     print("sli", sli)
        #     print("index", index)



















        # sli = 1
        # index = 0
        # prefix = ''
        # print(len(strs))
        # if len(strs) == 1:
        #     return strs[0]
        # for i in range(len(strs)-1, -1, -1):
        #     pre = strs[index][0:sli]
        #     # print("strs", strs)
        #     print("pre", pre)
        #     for j in range(len(strs)-1, -1, -1):
        #         if pre == strs[j][0:sli]:
        #             prefix = pre
        #             # continue
        #         elif pre != strs[j][0:sli]:
        #             break
        #     sli += 1
        #     index += 1
        #     return prefix

# def romanToInt(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     sum_rom = 0
#     romInt = {u'I':1, u'V':5, u'X':10, u'L':50, u'C':100, u'D':500, u'M':1000}
#     for i in range(len(s)-1, -1, -1):
#         if (i+1) < len(s):
#             if s[i]== 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
#                 sum_rom += -romInt.get(s[i])
#             elif s[i]== 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
#                 sum_rom += -romInt.get(s[i])
#             elif s[i]== 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
#                 sum_rom += -romInt.get(s[i])
#             else:
#                 sum_rom += romInt.get(s[i])
#         else:
#             sum_rom += romInt.get(s[i])
#     print("result", sum_rom)



# def romanToInt(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     st = list(s)
#     sum_rom = 0
#     romInt = {u'I':1, u'V':5, u'X':10, u'L':50, u'C':100, u'D':500, u'M':1000}
#     for i in range(len(st)):
#         print(i)
    #     if (i+1) < len(st) and romInt.get(st[i]) < romInt.get(st[i+1]):
    #             sum_rom += - romInt.get(st[i])
    #     else:
    #         sum_rom += romInt.get(st[i])
    # print("sum_rom", sum_rom)

# def romanToInt(s: str) -> int:
#     result, nums = 0, {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     for i in range(len(s) - 1, -1, -1):
#         if i != len(s) - 1 and nums[s[i]] < nums[s[i + 1]]:
#             result -= nums[s[i]]
#         else:
#              result += nums[s[i]]
#     print("result", result)

# romanToInt("MCM")
















# def longestCommonPrefix(strs):
#         """
#         :type strs: List[str]
#         :rtype: str
        # """
        # sli = 1
        # pre = ""
        # print("strs", strs)
        # print(len(strs))
        # count_str = 0
        # if len(strs) == 1:
        #     count_str = len(strs)
        # elif len(strs) > 1:
        #     count_str = len(strs)-1
        #
        # for i in range(len(strs)):
        #     if len(strs) > 1 and strs[i][0:sli] == strs[i+1][0:sli]:
        #         print("Hello")
        #         print("ount_str", count_str)
        #         print(strs[i][0:sli], strs[i+1][0:sli])
        #         pre = strs[i][0:sli]
        #         sli += 1
        #     elif len(strs) == 1:
        #         print(len(strs))
        #         pre = strs[i]
        # print("pre", pre)
        # return pre

        # sli = 1
        # pre = ""
        # for i in range(len(strs)):
        #     if len(strs) != i:
        #         print("Hello")
        #         if len(strs) > 1 and strs[i][0:sli] == strs[i+1][0:sli]:
        #             pre = strs[i][0:sli]
        #             sli += 1
        #         elif len(strs) == 1:
        #             pre = strs[i]
        # print("pre", pre)
        # return pre

# longestCommonPrefix(["flower","flow","flight"])
