def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # if len(s) == 1 or numRows <= 1:
        #     return s
        #
        # interval = 2*numRows - 2
        # zigZag = []
        # index = 0
        # for i in range(numRows):
        #     step = interval - 2*i
        #     # print('step', step)
        #     j = i
        #     while j<len(s):
        #
        #         print(j, step)
        #         zigZag.append(s[j])
        #         if step > 0 and step < interval and j + step < len(s):
        #             zigZag.append(s[j+step])
        #         # print(interval)
        #         j += interval
        # return ''.join(zigZag)

                # j = i

                # zigZag.append(s[j])
        # print('zigZag', zigZag)
        result = ['']*numRows

        j = 0
        for i in s:
            # print(i, 'result', result[j])
            result[j] = result[j] + i
            # print(result[j], i)
            if j==0:
                m = j
                j += 1
                print(j, m)
            elif (j == numRows-1) | (j-m<0):
                print(j, numRows-1, j-m)
                m = j
                j -= 1
            else:
                m = j
                j += 1
        return ("".join(result))

print(convert("PAYPALISHIRING", 3))
