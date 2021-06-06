class PartyAnimal:
    x = 0
    name =''
    def __init__(self, name):
        self.name = name
    def party(self):
        self.x =self.x +1
        print('party count for', self.name,'is',self.x)


class FootballFan(PartyAnimal):
    points = 0
    def goals(self):
        self.points = self.points + 5
        print('No. of goals:', self.points)
        self.party()


s = PartyAnimal('Sally')
j = FootballFan('Joe')

s.party()
j.goals()
