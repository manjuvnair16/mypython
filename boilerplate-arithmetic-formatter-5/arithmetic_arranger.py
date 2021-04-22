import re
def arithmetic_arranger(problems, req_answer = False):
  arranged_problems = ""
  #if there are too many problems
  if len(problems) > 5:
    error_str = 'Error: Too many problems.'
    return error_str

  lst = list()
  newlst = list()

  #printing line 1
  for each_problem in problems:
    # in case of multiplication or division
    if re.search('[*/]',each_problem):
      error_str = "Error: Operator must be '+' or '-'."
      return error_str

    #in case of the presence of non-numeric characters
    if re.search('[^\s0-9+-]',each_problem):
      error_str = "Error: Numbers must only contain digits."
      return error_str

    #in case of more than 4 digits
    if re.search('\d{5,}',each_problem):
      error_str = "Error: Numbers cannot be more than four digits."
      return error_str

    answer = eval(each_problem)
    lst = each_problem.split(' ')

    #length is needed later to determine the no. of spaces to be added before printing the smaller operand
    len_operand1 = len(lst[0])
    len_operand2 = len(lst[2])

    if len_operand1 >= len_operand2:
        lst.append(0)                       #0 is value at lst[3] if first operand has more or equal no. of digits
        n = len_operand1 - len_operand2 + 1 #needed to print the no. of spaces in the second line of operands after the operator sign (1 signifies the space after the operator sign)
        line1 = ' ' * 2 + lst[0]
    else:
        lst.append(2)                       # 2 is value at lst[3] if second operand has more no. of digits
        n = len_operand2 - len_operand1 + 2 #2 is added at the end for 2 spaces for operator and a space after that.
        line1 = ' ' * n + lst[0]

    #print(line1 + ' ' * 4 ,end='') # print line1 and leave 4 spaces between each problem
    arranged_problems += line1 + ' ' * 4
    lst.append(n)                  #n is the no. of spaces needed to be added in line 2
    lst.append(answer)             #answer is for line 4 if asked to evaluate i.e if req_answer = True
    newlst.append(lst)             #lst has the original equation string with the above 3 values appended to it: lst = [operand1, operator, operand2, 0/2, n, answer]
  #print('')                          #goes to next line
  arranged_problems = arranged_problems.rstrip(' ')
  arranged_problems += '\n'

  #printing line 2
  len_line2 = list()                                #length of line 2 is required to determine the no. of seperators '-' needed on the next line
  for item in newlst:
    if item[3] == 2:                              # operand 2 is bigger
        line2 = item[1]+ ' ' + item[2]            #operator + space + operand 2
    else:                                         #operand 1 is bigger
        line2 = item[1] + ' ' * item[4] + item[2] #operator + space * (item[4] = len_operand1 - len_operand2 + 1) + operand 2

    #print(line2 + ' ' * 4,end='')                 # print line2 and leave 4 spaces between each problem
    arranged_problems += line2 + ' ' * 4
    len_line2.append(len(line2))
  #print('')                                         # goes to next line
  arranged_problems = arranged_problems.rstrip(' ')
  arranged_problems += '\n'

  #printing line 3 (seperator line -----)
  for length in len_line2:
    sep = '-'* length
    #print(sep + ' ' * 4,end='')
    arranged_problems += sep + ' ' * 4
  #print('')
  arranged_problems = arranged_problems.rstrip(' ')
  

  #printing line 4 (answers if needed)
  if req_answer == True:
    arranged_problems += '\n'
    for item,line in zip(newlst,len_line2):    #iterate through newlst and len_line2 to get the answer and the length of line 2
        n = line - len(str(item[5]))           # n  = no. of spaces needed to be added before printing answer
        answer_line = ' ' * n + str(item[5])
        #print( answer_line + ' ' * 4,end='')
        arranged_problems += answer_line + ' ' * 4
    arranged_problems = arranged_problems.rstrip(' ')

  return arranged_problems