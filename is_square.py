# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def is_square(n):
    '''Determines if the given number is a perfect square.

    Uses the property of perfect square numbers that for a given number n,
    the square root of n is equal to the total of the first (square root of n) odd numbers starting from 1.
    For example, n = 3 is not a perfect square because 1 + 3 + 5 (the first 3 odd numbers, starting from 1) = 9.
    However, 4 is a perfect square because 1 + 3 = 4(2-squared)'''
    logging.debug("n = " + str(n))
    if (n < 0):
        # negative numbers cannot be perfect squares
        return False
    #if (n == 0 or n == 1):
    if (n == 0 or n == 1):
        # 0 and 1 are perfect squares
        return True
    result = 0
    for i in xrange(1, n, 2):
        logging.debug("loop = " + str(i))
        result += i
        logging.debug("result = " + str(result))
        # if (result == n and j == n):
        if (result == n):
            logging.debug("result == n, returning True.")
            return True
        elif (result > n):
            logging.debug("result > n, returning False")
            return False
        else:
            continue
    if (result < n):
        logging.debug("result = " + str(result))
        return False
    return None

is_square(-1)
is_square(0)
is_square(1)
is_square(3)
is_square(4)
is_square(25)
is_square(26)
# is_square(946729)
