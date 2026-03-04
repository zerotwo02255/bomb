class P:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hlo(self):
        self.age +=1
        print(f"happy birthday {self.age}")

p1=P("jedd",2)
p1.hlo()
p1.hlo()
p1.hlo()
p1.hlo()