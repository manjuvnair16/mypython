filehandle = open('mbox-short.txt')
for line in filehandle:
    line = line.rstrip()
    word_list = line.split()
    if len(word_list) > 0 and word_list[0] == 'From':
        print(word_list[2])
