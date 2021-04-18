filehandle = open('mbox-short.txt')
for line in filehandle:
    line = line.rstrip()
    print(line.upper())
    
