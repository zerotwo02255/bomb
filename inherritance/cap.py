class person:
     def __init__(self,brand,model):
        self.brand=brand
        self.__model=model
     def get_model(self):
         return self.__model
     
     def set_model(self,model):
         self.__model=model
p1=person("kale","malee")
print(p1.get_model())

p1.set_model("saale")
print(p1.get_model())