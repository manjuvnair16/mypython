
file_name = input('Enter file name:')
if len(file_name) < 1:
    file_name ='clown.txt'
file_handle = open(file_name)
count_words = dict()
for line in file_handle:
    line.rstrip()
    word_list = line.split()
    for word in word_list:
        count_words[word] = count_words.get(word,0) +1

print(count_words)

largest_count = -1
for word, count in count_words.items():
    if count > largest_count:
        largest_count = count
        frequent_word = word

print(frequent_word, largest_count)
