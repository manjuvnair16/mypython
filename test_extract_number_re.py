
# extract lines with 'X-DSPAM-Confidence: 0.8475',
#extract the number and find the max

import re
file_handle = open('mbox-short.txt')
lst = list()
for line in file_handle:
    line.rstrip()
    str_match = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(str_match) > 0:
        fnum = float(str_match[0])
        lst.append(fnum)
#print(lst)
print('Maximum:', max(lst))
