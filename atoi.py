def myAtoi(str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        # 4324swq
        atoi = 0
        neg = False
        start = 0
        if not str:
            return 0
        if str[0] == '-':
            neg = True
            start = 1
        elif str[0] == '+':
            neg = False
            start = 1
        elif str[0].isdigit() == False:
            return 0
        for i in range(start, len(str)):
            if str[i].isdigit():
                atoi = atoi*10 + ord(str[i]) - ord('0')
            else:
                break
        if neg:
            atoi *= -1
        if neg and atoi < -2147483648:
            return -2147483648
        elif neg == False and atoi > 2147483647:
            return 2147483647
        else:
            return atoi

        # if str
print("returning", myAtoi(""))
# if int(atoi) > 2147483647:
#     return  2147483647
# elif int(atoi) < -2147483648:
#     return -2147483648
# else:
#     return int(atoi)
