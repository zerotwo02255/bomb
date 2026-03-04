class car:
    def __init__(self,anime_name,anime_age):
        self.animename=anime_name
        self.animeage=anime_age
    def show(self):
        print(self.animename,self.animeage)

class bike(car):
    def __init__(self, anime_name, anime_age,power):
        super().__init__(anime_name, anime_age)
        self.power=power

    def welcome(self):
        print(f"hello my name is {self.animename} and i am {self.animeage} and my power is {self.power}")    

p1=bike("naruto",40,"rasengan")
p1.welcome()
