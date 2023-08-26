class Animal:
    def __init__(self, name: str, breed: str, age: int) -> None:
        self.name = name
        self.breed = breed
        self.age = age
    def voice(self):
        print('Animal\'s voice')

class Cat(Animal):
    weight = 5 #Інкапсуляція, public type
    _height = 35 #Інкапсуляція, protected type
    __coat_color = 'grey' #Інкапсуляція, privat type
    def voice(self):
        print('Meow') 
    parameters = (weight, _height, __coat_color)

class Dog(Animal):
    weight = 18
    _height = 45
    __coat_color = 'white'
    parameters = (weight, _height, __coat_color)

cat = Cat('Mary', 'Maine Coon', 5) 
dog = Dog('Max', 'Chow-chow', 4) # Абстракція, адже усі дочірні класи класу Animal обов'язково мають параметри name, breed та age


print(cat.name, cat.breed, cat.age, cat.parameters)
print(dog.name, dog.breed, dog.age, dog.parameters)
cat.voice() # Поліморфізм, адже клас Cat наслідує метод voice від класу Animal, але змінює поведінку
dog.voice() # Наслідування, адже у класі Dog немає методу voice, але він наслідує його від класу Animal