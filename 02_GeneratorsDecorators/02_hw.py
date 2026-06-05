# Завдання 1
# Створіть функцію, яка повертає всі непарні числа в діапазоні. Функція приймає початок і кінець діапазону як параметри. 
# Використовуйте механізм генераторів усередині функції.
print("Task 1")
start = int(input("enter start: "));
end = int(input("enter end: "));

def oddNums(start,end):
    while (start <= end):
        if (start % 2 != 0):
          yield start
        start+=1;

for item in oddNums(start,end):
    print(item,"\t")

# Завдання 2
# Створіть функцію, яка повертає всі значення зі списку, що не перебувають у діапазоні, зазначеному користувачем. 
# Функція приймає список, початок і кінець діапазону як параметри. Використовуйте механізм генераторів усередині функції.
print("Task 2")
start1 = int(input("enter start: "));
end1 = int(input("enter end: "));

def outOfRangeNums(start,end):
    print()
    i = 0;
    while i < start:
        yield i;
        i+=1;
    j = end
    print()
    for j in range(10):
        yield j
        j+=1

for item in outOfRangeNums(start1,end1):
    print(item,end="\t")

# Завдання 3
# Для виконання цього завдання обов'язково використовуйте механізм функцій вищого порядку (higher order functions). 
# Створіть функцію, що відображає лінію (горизонтальну або вертикальну) з використанням символу, 
# зазначеного користувачем. Користувач визначає символ і яку лінію відображати.
# Сигнатура функції:
# def show_line (symbol, function_to_call)
# symbol - символ для відображення.
# function_to_call - функція для відтворення лінії (вертикальна лінія або горизонтальна лінія, на один тип лінії - одна функція).
print("Task 3")
def drawLine(symbol,style):
    if(style=="horizontal"):
        for i in range(10):
            print(symbol, end="")
    if (style=="vertical"):
        for i in range(10):
            print(symbol)

symb = input("enter symbol: ")
st = input("enter style (horizontal/vertical): ")

def getValues(func):
    return func(symb,st)

getValues(drawLine)

# Завдання 4
# Створіть функцію, що повертає список з усіма парними числами, від 0 до 100000.
# Використовуючи механізм декораторів, порахуйте скільки секунд знадобилося для обчислення всіх чисел. Відобразіть на екран кількість секунд і всі парні числа від 0 до 100000.

print("Task 4")
import time
def decorator(func):
    def private_decorator():
        start = time.time();
        func()
        end = time.time();
        print(f"Time elapsed {end-start} s")
    return private_decorator;

@decorator
def evenList():
    for i in range(10000):
        if (i %2 == 0):
            print(i , end="\t")
        i+=1;
    print()
    return
evenList()

# Завдання 5
# Додайте до четвертого завдання можливість передавати межі діапазону для пошуку всіх парних чисел.

print("Task 5")
start2 = int(input("enter start: "));
end2 = int(input("enter end: "));

def decoratorRange(func):
    def private_decorator(*args,**kwargs):
        start = time.time();
        func(*args,**kwargs)
        end = time.time();
        print(f"Time elapsed {end-start} s")
    return private_decorator;
@decoratorRange
def evenListRange(start,end):
    for i in range(start,end):
        if (i %2 == 0):
            print(i , end="\t")
        i+=1;
    print()
    return

evenListRange(start2,end2)
