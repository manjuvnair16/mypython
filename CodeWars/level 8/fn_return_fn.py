#function returning a function
def always(n=0):
    return lambda  : n

one = always(1)
print(one())

'''console log
1
'''

'''
-------------------------------
Alternate Solutions
-------------------------------
def always(n=0):
    return lambda x=n: x
    

def always(n=0):
    def a():
        return n
    return a
