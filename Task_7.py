class Animal:
    count = 0  # Статическая переменная для подсчета экземпляров

    def __init__(self):
        Animal.count += 1  # Увеличиваем счетчик при создании нового экземпляра

    @staticmethod
    def get_count():
        return Animal.count  # Возвращаем количество экземпляров

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

# Вызываем статический метод для получения количества экземпляров
print("Количество созданных экземпляров:", Animal.get_count())

