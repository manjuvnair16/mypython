count = 0
sum = 0
while True:
  input_value = input('Enter a number:')
  if input_value == 'done':
    break
  else:
    try:
      num = float(input_value)
    except:
      print('Enter a number or done')
      continue
    count = count + 1
    sum = sum + num

avg = sum / count
print(count, sum, avg)
