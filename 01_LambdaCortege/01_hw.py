# Завдання 1
# Маємо три кортежі цілих чисел. Знайдіть елементи, які є у всіх кортежах.
# Завдання 2
# Маємо три кортежі цілих чисел. Знайдіть елементи, які унікальні для кожного списку.
# Завдання 3
# Маємо три кортежі цілих чисел. Знайдіть елементи, які є в кожному з кортежів і знаходяться в кожному з них на тій самій позиції.

print("Task 1")
t1 = (69,569,89,69,85,51,5647,56)
t2 = (97,569,69,874,15,85,56,52)
t3 = (12,569,85,41,23,56,32,15)

arr1 = set(); 

for i in t1:
 for j in t2:
    if i==j:
        for k in t3:
         if k==i:
             arr1.add(k)
             break;
    
print(f"Repeating elems: {arr1}")


print("Task 2")
arr2 = set();

for i in t1:
 if(t2.__contains__(i) or t3.__contains__(i) ):
   pass;
 else:
   arr2.add(i)

for j in t2:
 if(t1.__contains__(j) or t3.__contains__(j) ):
   pass;
 else:
   arr2.add(j)

for k in t3:
 if(t1.__contains__(k) or t2.__contains__(k) ):
   pass;
 else:
   arr2.add(k)


print(f"Unique elems: {arr2}")


print("Task 3")
arr3 = set()
for i in range(len(t1)):
 if (t1[i]==t2[i]==t3[i]):
   arr3.add(t1[i])
 i+=1;  

print(f"Elems at same palces: {arr3}")