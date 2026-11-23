class animal:
    def __init__(self, name , species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class cat(animal):
    def __init__(self, name , breed):
        animal.__init__(self,name,species="cat")

    def make_sound(self):
        print("Meoww")

c = cat("pussy","russian")
c.make_sound()
