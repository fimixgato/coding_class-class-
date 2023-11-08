class Lion():
    def __init__(self,name,age,adress,hobby,dislikes,lioness):
        self.name=name
        self.age=age
        self.adress=adress
        self.hobby=hobby
        self.dislikes=dislikes
        self.lioness=lioness

    def Introduce(self):
        print(f"The name of this lion is {self.name}")
    def location(self):
        print(f"{self.name} is located in {self.adress}")
    def years(self):
        print(f"{self.name} is {self.age}")
    def eat(self):
        print(f"{self.name} loves to {self.hobby}")
    def hate(self):
        print(f"{self.name} hates {self.dislikes}")
    def hunt(self):
        print(f"{self.name} has the sole duty to hunt for his family")
    def girlfriend(self):
        print(f"{self.name} and his mate {self.lioness} always share their food.")
    def bathe(self):
        print(f"While {self.lioness} has the duty of bathing the cubs")
    def cub(self):
        print(f"The cubs have to eat if they will grow to be like their father {self.name}")
    def end(self):
        print(f"Thank you so much for reading this short article about the life of {self.name}")

my_lion=Lion("Simba", "15 years old", "Sahara Desert", "eat", "Hyenas and Elephants", "Stacy")
my_lion.Introduce()
my_lion.location()
my_lion.years()
my_lion.eat()
my_lion.hate()
my_lion.hunt()
my_lion.girlfriend()
my_lion.bathe()
my_lion.cub()
my_lion.end()