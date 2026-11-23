class MyClass:
    def __init__(self,value):
        self._value = value
    def show(self):
        print(f"Value is {self._value}")

    @property   # kyuki ten_value nam ka jo soda h vo is property k ander h to ise m getter khunga
    def ten_value(self):
        return 10* self._value

    @ten_value.setter # or m ten value jo prop. k ander tha use as a decorator bhi use kr rha hu .setter lgake or fir rewrite bhi kr rha hu 
    # this is known as setter 
    def ten_value(self, new_value):
        self._value = new_value/10

obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()
# bhai ynha confuse mt hona jo ten_value return kr rha h vo hi new_value h. or ye bakchodi chalti rhni chaiye
