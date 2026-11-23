# public variable = sare k sare variable public hi hote h python me bs ek chota sa exception h mtlb kh skte h use ki ye public nhi hai
class employee:
    def __init__(self):
        self.name = "Harry"
obj1 = employee()
print(obj1.name)
# ye thi aam jindegi ki bhai normal si bat hai

# lekin m chahata hu ki jo ye variable h use koi access krne lge to se ek warning type aaye ki nah bhai nah ye achi bat nhi hai 
# ha lekin kr to vo tbhi bhi skta hai acess
 
# Aaisi cheejo ko private variable khte hai
class chutiya:
    def __init__(self):
        self.__name = "Lucky"
obj2 = chutiya()
# print(obj2.__name) # bhai ye error dega agr chalaga to mtlb keh rha hai ki bhdk ye meri private cheej hai
# private cheej mtlb ijjat hai or ijjat lutne me to hme bhot mja aata hai
# to le ladle tu bhi __name ko to access krke rhenge
print(obj2.__dir__())
print(obj2._chutiya__name) # dekh ynha keh rhe hai ki error aayega mtlb ruk ja bhdk
# pr acess ho jayga.....

# ek protected bhi hote hai
class gandwa:
    def __init__(self):
        self._name = "Aman"

obj3 = gandwa() 
print(obj3._name) 
# bhai in    _var valo ko protected khte h pta nhi kyu lekin hai to hai 
# han ye bhi easily/directly accessable hai
