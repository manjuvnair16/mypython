import copy
import random


class Hat:
#initialise contents with the input given through key-word arguments {"red" = 2 ,"blue" = 3}
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)         #contents is a list of colours with count of each colour in the list = value

  #draw no_of_balls from contents randomly, remove drawn balls from contents and return the list of drawn balls
  def draw(self, no_of_balls):
    if no_of_balls >= len(self.contents):  #if no_of_balls is greater than no of balls in contents, return contents
      return self.contents
    else:
      drawn_balls = []
      for i in range(no_of_balls):
        pick_ball = random.choice(self.contents)
        drawn_balls.append(pick_ball)
        self.contents.remove(pick_ball)
      return drawn_balls


#function to draw balls randomly from contents and check if drawn balls meet expected_balls criteria,
#calculate probability = number of times criteria met / number of times experiment performed and,
#return probability
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  meets_expctd_balls_cnt = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)                 #copy.deepcopy ensures that even though draw() changes the contents variable, it is reset before each experiment
    drawn_balls = hat_copy.draw(num_balls_drawn)
    expctd_is_actual = False
    for colour, total_balls in expected_balls.items():
      cnt_value = drawn_balls.count(colour)
      if cnt_value >= total_balls:                #if expected count for a colour is met set the var expctd_is_actual = True
        expctd_is_actual = True
      else:
        expctd_is_actual = False                  #else set expctd_is_actual = False and break as there is no need to check for other colours
        break
    if expctd_is_actual == True:
      meets_expctd_balls_cnt += 1                 #if the criteria for all the expected_balls is met, increase the count

  prob = (meets_expctd_balls_cnt/num_experiments) #cal probability
  return prob
