#find returns the position of the char
#str[col_pos+1:] slices the string starting from col_pos till the end of string
#strip() removes any white space from the start and end of the string

str = 'X-DSPAM-Confidence: 0.8475'
col_pos = str.find(':')
num_str = str[col_pos+1:]
fnum = float(num_str.strip())
print(fnum)
