#print the count of first five largest frequency words

file_name = input('Enter file name:')
if len(file_name) < 1:
    file_name ='clown.txt'
file_handle = open(file_name)
count_words = dict()
for line in file_handle:
    line.rsplit()
    word_list = line.split()
    for each_word in word_list:
        count_words[each_word] = count_words.get(each_word,0) + 1
#print(count_words)

#first method to flip the tuple, sort it and flip it back again
lst = list()
#print(count_words.items())
for k,v in count_words.items():
    new_tuples = (v,k)
    lst.append(new_tuples)

lst = sorted(lst, reverse=True)
#print(lst)
for v,k in lst[:5]:
    print(k,v)

print('The second method for the same functionality')
#second method to flip, sort and re-flip the tuple
new_lst = sorted([(v,k) for k,v in count_words.items()],reverse=True)
for v,k in new_lst[:5]:
    print(k,v)
