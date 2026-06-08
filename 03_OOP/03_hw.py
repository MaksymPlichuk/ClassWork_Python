# Завдання 1
# Реалізуйте клас «Автомобіль». Збережіть у класі: назву моделі, рік випуску, виробника, об'єм двигуна, колір машини, ціну.
#  Реалізуйте методи класу для введення-виведення даних та інших операцій.
print("\nTask1")
class Car:
    def __init__(self, name="", year="", manufacturer="", volume="", color="", price=""):
      self.name = name
      self.year = year
      self.manufacturer = manufacturer
      self.volume = volume
      self.color = color
      self.price = price
    def makeCar(self):
      self.name = input("Enter Car name: ")
      self.year = input("Enter Year: ")
      self.manufacturer = input("Enter manufacturer: ")
      self.volume = input("Enter volume: ")
      self.color = input("Enter color: ")
      self.price = input("Enter price: ")
    def __str__(self):
       return f"\nCar name: {self.name}, year: {self.year},\nManufacturer: {self.manufacturer}, \nVolume: {self.volume}, Color: {self.color}, price: {self.price}"

car = Car()
car.makeCar()
print(car)

# Завдання 2
# Реалізуйте клас «Книга». Збережіть у класі: назву книги, рік видання, видавця, жанр, автора, ціну. Реалізуйте методи класу
#для введення-виведення даних та інших операцій.
print("\nTask2")
class Book:
    def __init__(self, name="", year="", publisher="", genre="", author="", price=""):
      self.name = name
      self.year = year
      self.publisher = publisher
      self.genre = genre
      self.author = author
      self.price = price
    def makeBook(self):
      self.name = input("Enter Book name: ")
      self.year = input("Enter Year: ")
      self.publisher = input("Enter publisher: ")
      self.genre = input("Enter genre: ")
      self.author = input("Enter author: ")
      self.price = input("Enter price: ")
    def __str__(self):
       return f"\nBook name: {self.name}, year: {self.year},\npublisher: {self.publisher}, \ngenre: {self.genre}, author: {self.author}, price: {self.price}"
   
book = Book()
book.makeBook()
print(book)   

# Завдання 3
# Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість. 
# Реалізуйте методи класу для введення-виведення даних та інших операцій.
print("\nTask3")
class Stadium:
   def __init__(self, name="", openningYear="", city="", capacity=""):
      self.name = name
      self.openningYear = openningYear
      self.city = city
      self.capacity = capacity
   def makeStadium(self):
      self.name = input("Enter Stadium name: ")
      self.openningYear = input("Enter openningYear: ")
      self.city = input("Enter city: ")
      self.capacity = input("Enter capacity: ")
   def __str__(self):
       return f"\nStadium name: {self.name}, openningYear: {self.openningYear},\ncity: {self.city}, \ncapacity: {self.capacity}"

stad = Stadium()
stad.makeStadium()
print(stad)