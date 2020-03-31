# def countAndSay(n):
#     """
#     :type n: int
#     :rtype: str
#     """
#     if n == 1:
#         return '1'
#     s = '1'
#     track = n
#     countandsay = []
#     counter = 0
#     print('s[0]', s[0])
#
#     # 1113213211
#     while track > 1:
#         print('s', s)
#         pointer = s
#         countandsay = []
#         for i in range(n):
#             print('i:', i, 's:', s)
#             if i < len(s):
#                 print('i', i, n, countandsay, 's[i]', s[i], 'pointer', pointer)
#                 if s[i] == pointer:
#                     print('in if', countandsay, s[i], pointer)
#                     counter += 1
#                 else:
#                     countandsay.append(str(counter))
#                     countandsay.append(pointer)
#                     print('in else', countandsay, s[i], pointer)
#                     counter = 1
#                     pointer = s[i]
#                     # track -= 1
#             else:
#                 print('i in break:', i)
#                 break
#         # counter += 1
#         print('out while', 'counter:', counter, 'pointer:', pointer, 's:', s, 'track', track)
#         # if n >= 9 and track==2:
#         #     counter += 1
#         # countandsay.append(str(counter))
#         # countandsay.append(pointer)
#         s = ''.join(countandsay)
#         counter = 0
#         track -= 1
#     print('s', s, 'countandsay', countandsay)
#     return s
#
# print(countAndSay(4))
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 6.     312211
# 7.     13112221
# 8.     1113213211 1113213211
# 9.     31131211131221 31131211131211
# 10.    13211311123113112211 13211311123113

# def countAndSay(n, track, s):
#     """
#     :type n: int
#     :rtype: str
#     """
#     s = s
#     track = track
#     counter = 0
#     pointer = s[0]
#     countandsay = []
#     print('s', s)
#
#     print('track', track, n)
#     if track == 1:
#         return countandsay
#
#     for i in range(n):
#         if i < len(s):
#             print('i', i, n)
#             if s[i] == pointer:
#                 counter += 1
#                 print('in if', countandsay, s[i], pointer)
#             else:
#                 countandsay.append(str(counter))
#                 countandsay.append(pointer)
#                 print('in else', countandsay, s[i], pointer)
#                 counter = 1
#                 pointer = s[i]
#     countandsay.append(str(counter))
#     countandsay.append(pointer)
#     track -= 1
#     return countAndSay(n, s=''.join(countandsay), track=track)
#
# countAndSay(9, track=9, s='1')

## index out of range
# def countAndSay(n):
#     finalString = '1'
#
#     if n == 1:
#         return finalString
#     pointer = 0
#     counter = 0
#     stringInProcess = ''
#     while n>1:
#         while counter < len(finalString):
#             print('pointer', pointer)
#             if pointer < len(finalString):
#                 while finalString[pointer] == finalString[counter]:
#                     print('hello')
#                     counter += 1
#                 # counting the number of nums
#                 stringInProcess += str(counter - pointer)
#                 stringInProcess += finalString[pointer]
#                 pointer = counter
#
#         # print('stringInProcess', stringInProcess)
#         finalString = stringInProcess
#         stringInProcess = ''
#         pointer = 0
#         counter = 0
#         n-=1
#     return finalString
#
# print('>>>>>>>>>', countAndSay(3))




def countAndSay(n):
    countandsay = '1'
    if n==1:
        return countandsay
    pointer = 0
    counter = 0
    stringInProcess = ''
    while n > 1:
        while counter<len(countandsay):
            while countandsay[pointer] == countandsay[counter]:
                counter+=1
                if counter >= len(countandsay):
                    break
            stringInProcess += str(counter-pointer)
            stringInProcess += countandsay[pointer]
            pointer = counter
            if pointer >= len(countandsay):
                break
        countandsay = stringInProcess
        stringInProcess = ''
        pointer = 0
        counter = 0

        print('stringInProcess', countandsay)
        # 31131211131221
        n-=1
    return countandsay
print(countAndSay(9))
