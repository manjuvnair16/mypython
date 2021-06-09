#implement a switch case in python
def get_planet_name(id):
    
    def mercury():
        return "Mercury"
    
    def venus():
        return "Venus"

    def earth():
        return "Earth"
    
    def mars():
        return "Mars"
    
    def jupiter():
        return "Jupiter"
    
    def saturn():
        return "Saturn"
    
    def uranus():
        return "Uranus"
    
    def neptune():
        return "Neptune"
    
    def default():
        return "Incorrect input"
    
    
    switcher = {
        1 : mercury ,
        2 : venus,
        3 : earth,
        4 : mars,
        5 : jupiter,
        6 : saturn,
        7 : uranus,
        8 : neptune
    }
    
    return switcher.get(id,default)()
  
  get_planet_name(2)
  
  '''console log
  Venus
  '''
  
  '''
  ------------------------------------
  Alternate solutions
  ------------------------------------
  def get_planet_name(id):
    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus", 
        8: "Neptune",
    }
    return planets[id]
    
  def get_planet_name(id):
    return {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id, None)
    
  def get_planet_name(id):
    return ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"][id-1]
