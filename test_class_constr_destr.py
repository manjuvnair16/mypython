class PartyAnimal:
    cnt = 0
    name =''
    def __init__(self,z):
        self.name = z
        print(self.name,'is constructed')
    def party(self):
        self.cnt = self.cnt + 1
        print(self.name,'Party Count:',self.cnt)

    def __del__(self):
        print('obj', self.name,'has been destructed')

s = PartyAnimal('Sally')
j = PartyAnimal('Joe')

s.party()
j.party()
s.party()

j.cnt=s.cnt
j.party()
