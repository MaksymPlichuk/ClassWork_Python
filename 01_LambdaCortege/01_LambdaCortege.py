#---------------------dictionary
student = {
    "name": "ivan",
    "age": 52
}

print(student["name"])
student["mail"]= "dsasdadasasd@fafsad"
print(student)

del student["mail"]
print(student)

for key in student:
    print(f"{key}: {student[key]}")

#---------------------------------- lambda
mysqr = lambda x: x*x
print(mysqr(2))

def square(num):
    return num*num
print(square(2))



arr = [
    {"name":"ivan", "age":65},
    {"name":"asd", "age":45},
    {"name":"bob", "age":12}
]

arr.sort(key=lambda x: x["age"])
print(arr)

sorted = sorted(arr, key=lambda st: st["age"])
print(sorted)

print(type(arr[0]))
#---------------------------tuple

myTuple = (45,25,478)

try:
    myTuple[0] = 178
except TypeError as e:
    print("Error")

print(f"Cortege count: {len(myTuple)}")

for item in myTuple:
    print("Elem: ", item)

i=0
while(i < len(myTuple)):
    print(myTuple[i])
    i+=1