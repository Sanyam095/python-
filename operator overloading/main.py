class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):
        return Vector(self.i+x.i , self.j+x.j , self.k+x.k ) # dekh jo meine ynha kiya na uska explanation niche ki do lines me hai

v1 = Vector(3,5,6)
print(v1)

v2 = Vector(1,2,9)
print(v2)


print(v1 + v2)
print(type(v1+v2)) # bhai do vectors ko agr add kroge to aap ye nhi chahoge ki vo string aaye aap chahoge ki vo vector hi aaye 
# Taki vector aaye esiliye hm vector constructor ka istemal krenge....
