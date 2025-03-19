class Animal:
    def voice(self):
        pass
# Создаем классы-наследники
class Dog(Animal):
    def voice(self):
        return 'Гав!'

class Cat(Animal):
    def voice(self):
        return 'Мяу!'

class Tiger(Animal):
    def voice(self):
        return 'PPP!'

# Создаем экземпляры классов
dog = Dog()
cat = Cat()
tiger = Tiger()

# Вызываем метод voice() для каждого экземпляра
print(dog.voice())
print(cat.voice())
print(tiger.voice())