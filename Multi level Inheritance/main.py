class animal:
    def __init__(self,name,species):
        self.name = name
        self.species= species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")


class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self,name,species="Dog")
        self.breed = breed

    def show_details(self):
        animal.show_details(self)
        print(f"Breed: {self.breed}")

class goldenRetriever(dog):
    def __init__(self,name,color):
        dog.__init__(self,name,breed="GoldenRetriever")
        self.color = color

    def show_details(self):
        dog.show_details(self)
        print(f"Color: {self.color}")

o = goldenRetriever("tommy", "black")
o.show_details()

#Output: 
# Name: tommy
# Species: Dog
# Breed: GoldenRetriever
# Color: black
# isme sbhi k gun hai...........
