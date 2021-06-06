#for a number as an input, return the largest possible number one can make with its digits.

def descending_order(num):
    num_arr = list(str(num))
    num_arr.sort(reverse = True)
    desc_num = ''.join(map(str,num_arr))
    return int(desc_num)
  
print(descending_order(45302))

'''console log
54320
'''

'''
------------------------------
Alternate solutions
------------------------------
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
    
    
    
def Descending_Order(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)
    
'''
