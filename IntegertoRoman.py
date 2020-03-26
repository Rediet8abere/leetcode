def intToRoman(num):
        """
        :type num: int
        :rtype: str
        """
        thousands = ['', 'M', 'MM', 'MMM']
        hunderds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        unit = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return thousands[(num%10000)//1000] + hunderds[(num%1000)//100] + tens[(num%100)//10] + unit[(num%10)]

print(intToRoman(58))
