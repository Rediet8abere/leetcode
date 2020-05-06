"""
    Keep subtracting the divisor from dividend until dividend becomes less than divisor.
    The dividend becomes the remainder, and the number of times subtraction is done becomes
    the quotient. Below is the implementation of above approach
"""
def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    print(float('inf'))
    if dividend >= float('inf'):
        return float('inf')
    elif dividend <= float('-inf'):
        return float('-inf')
    sign = 1
    if dividend < 0 and divisor > 0:
        sign *= -1
    elif dividend > 0 and divisor < 0:
        sign *= -1

    count = 0
    dividend = abs(dividend)
    divisor = abs(divisor)
    while dividend >= divisor:
        dividend -= divisor
        count += 1

    print("count: ", count*sign, "dividend: ", dividend)
divide(-2147483648, -1)
