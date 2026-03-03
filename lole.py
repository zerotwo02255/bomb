class P:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hlo(self):
        return f"{self.name}is {self.age} years old"

p1=P("kale",20)
print(p1.hlo())    