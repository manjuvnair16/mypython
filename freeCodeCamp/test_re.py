import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

#re.search returns true or false
if re.search('^From', x):
    print("found")
else:
    print('None')


#re.findall
y = re.findall('\S+@\S+',x)
print(y)

z = re.findall('^From (\S+@\S+)',x)
print(z)

xx = 'From: blah blah blah: test F3: string'
yy = re.findall('^F.+?:',xx)
print(yy)

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)
