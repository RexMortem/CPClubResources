#!/bin/python3

# For this, it's useful to know modulo (the remainder operator)
# Performing a division gives a remainder 

# 5 % 3 = 2 
# 5 % 2 = 1
# 8 % 2 = 0

# Dividing an integer by 2 gives you 0 as a remainder when even
# Dividing an integer by 2 gives you 1 when odd

# (n % 2) == 1 -> odd
# (n % 2) == 0 -> even

import math
import os
import random
import re
import sys

def Solution1(n): # Very literal solution
    if (n % 2) == 1: 
        print("Weird")
    elif ((n % 2) == 0) and (2 <= n <= 5): 
        print("Not Weird")
    elif ((n % 2) == 0) and (6 <= n <= 20):
        print("Weird")
    elif ((n % 2) == 0) and (n > 20): 
        print("Not Weird")
    
def Solution2(n): # Compressed solution
    if (n % 2) == 1: 
        print("Weird")
    elif (2 <= n <= 5) or (n > 20):
        print("Not Weird")
    else:
        print("Weird")

if __name__ == '__main__': # I split the solutions into separate functions
    n = int(input().strip())

    Solution2(n)
