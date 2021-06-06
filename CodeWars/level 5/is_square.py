#check if a given number is a square number

import math

def is_square(n):    
    if n >= 0:
      sq_root = math.sqrt(n)
      if sq_root.is_integer():
            return True
    return False
  
 print(is_square(106))
  
'''console log
False
'''

'''
------------------------------
Alternate Solutions
------------------------------
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;
    
    
import math
def is_square(n):    
    try:
        return math.sqrt(n).is_integer()
    except ValueError:
        return False
        
'''
