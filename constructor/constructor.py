class person:
    # name = "Sanyam"
    # occ = "Developer"
    def __init__(self, name , occ):
        print("Hey I am a person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("Harry", "Developer") # ynha teen arguments pass hue h bhdk ek harry ek developer or ek c as self smjha to agr tune upen niche arguments pass kiye to error!
b = person("Divya", "HR")
a.info()
b.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()
# constructor hmesha none return krta h