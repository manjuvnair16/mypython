# fibonacci series using a generator 

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
        
        
for count, value in enumerate(fib()):
    if count > 5:
        break
    print(value)
