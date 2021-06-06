smallest = None
for value in [9,41,12,3,74]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
print(smallest)
