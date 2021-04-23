class Category:
  name =''

  #initialise name/ledger/total funds and total withdrawals
  def __init__(self,name):
    self.name = name
    self.ledger = list()
    self.funds = 0
    self.total_withdrawals = 0


 #check funds method to check if amount is less or greater than total funds in a category
  def check_funds(self, amt):
    if self.funds >= amt:
      return True
    else:
      return False

#deposit given amount with a description
  def deposit(self, amt, desc = ""):
    detail = dict()
    detail["amount"] = amt
    detail["description"] = desc
    self.ledger.append(detail)
    self.funds += amt


#withdraw given amt if total funds is available with a description else do nothing
  def withdraw(self, amt, desc = ""):
    funds_avail = self.check_funds(amt)
    if funds_avail:
      detail = dict()
      detail["amount"] = (amt) * -1
      detail["description"] = desc
      self.ledger.append(detail)
      self.funds -= amt
      self.total_withdrawals += amt
      return True
    else:
      return False

#get the total withdrawn amount
  def get_total_withdrawals(self):
    return self.total_withdrawals

#get the balance amount
  def get_balance(self):
    return self.funds

#transfer amt from one category to another with a description
  def transfer(self, amt, cat_name):
    funds_avail = self.check_funds(amt)
    if funds_avail:
      self.withdraw(amt, "Transfer to " + cat_name.name)
      cat_name.deposit(amt,"Transfer from " + self.name )
      return True
    else:
      return False

#string representation of the object displayed on printing the object
  def __str__(self):
    title_line = "{:*^30s}\n".format(self.name)
    ldgr_items = ""
    for each_item in (self.ledger):
      ldgr_desc = "{:<23s}".format(each_item['description'][0:23])
      ldgr_amt = "{:>7.2f}\n".format(float(each_item['amount']))
      ldgr_items += ldgr_desc + ldgr_amt
    total_line = "Total: " + str(self.funds)
    prnt_obj = title_line + ldgr_items + total_line
    return prnt_obj




#function to display a bar chart of percentage spent on each category
def create_spend_chart(categories):
  total_withdrawn = 0      # variable to store the total of all the withdrawals from different categories
  cat_withdrawals = []     #list to store total withdrawals of each category
  catgry_names = []        #list to store names of categories - later needed to find the longest name
  cat_percent = []         #list to store percent withdrawal from each category

#get the total withdrawals and names of each category and find the sum to get total_withdrawn
  for i in range(len(categories)):
    cat_withdrawals.append(categories[i].get_total_withdrawals())
    catgry_names.append(categories[i].name)
    total_withdrawn += cat_withdrawals[i]

  #rounding percentage to nearest 10
  for each in cat_withdrawals:
    percent_withdrawn = int(each/total_withdrawn * 10)/10
    #percent_rounded = round(percent_withdrawn,-1)
    percent_rounded = int(percent_withdrawn * 100)
    cat_percent.append(percent_rounded)


#start appending the string to display the chart
  chart_title = "Percentage spent by category\n"   #chart title
  bar_chart = ""  #bar chart string
  y_axis = 100
  mark = [-1]  #to store the indices of categories which meets the y-axis: need this to add 'o' at each level below the point where the criteria of cat_percent = y_axis is met
  while y_axis >= 0:
    bar_chart += "{:>3}".format(str(y_axis)) + "| "   #prints '100| ', ' 90| ' and so on (3 spaces for number and is right aligned)
    for i in range(len(cat_percent)):
      if (int(cat_percent[i]) == y_axis) or (i in mark):  #if criteria met append with 'o + 2 spaces' else add '3 spaces'
        bar_chart += "o" + " "*2
        mark.append(i)
      else:
        bar_chart += " "*3

    bar_chart += "\n"
    y_axis -= 10

  chart_sep = " "*4 + "-" * (1+len(cat_withdrawals)*3)  #chart seperator starts after the '|', a category takes 3 placeholders(includes 2spaces)

#to display the category names
  longest_name = max(catgry_names, key = len)
  chart_name_str = ""                                  #chart x-axis labels
  for i in range(len(longest_name)):
    chart_name_str += "\n" + " "*5
    for each in catgry_names:
      if  i < len(each):                               #if the name ends, add 3spaces else print 1 char and 2 spaces
        chart_name_str += each[i] + " "*2
      else:
        chart_name_str += " "*3



  chart = chart_title + bar_chart + chart_sep + chart_name_str   #the output bar chart
  return chart
