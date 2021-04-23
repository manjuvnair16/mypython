class Rectangle:
  width = 0
  height = 0

  def __init__(self,width,height):
    self.width = width
    self.height = height

  def set_width(self, wdth):       
    self.width = wdth

  def set_height(self, ht):
    self.height = ht

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
    return diagonal

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return ("Too big for picture.")
    else:
      pic = ""
      for i in range(self.height):
        pic += '*' * self.width + '\n'
      return pic

  def get_amount_inside(self,shape):
    amount_inside = self.get_area() / shape.get_area()
    return int(amount_inside)

  def __str__(self):
    prnt_rect = "Rectangle(width=" + str(self.width) + ", " + "height=" + str(self.height) + ")"
    return prnt_rect


class Square(Rectangle):
  side = 0

  def __init__(self, sd):
    self.width = sd
    self.height = sd
    self.side = sd

  def set_side(self, side_ip):
    self.side = side_ip
    self.width = side_ip
    self.height = side_ip

  def __str__(self):
    prnt_sq = "Square(side=" + str(self.side) + ")"
    return prnt_sq

  def set_width(self,wide):
    self.width = wide
    self.height = wide
    self.side = wide

  def set_height(self,hght):
    self.width = hght
    self.height = hght
    self.side = hght
