print("Hello world /n")

# Get user input for name and print a personalized greeting.

name = input("Enter your name: ")
print("Hello," + name + "!")

# Variable and datatypes

age = 22
print("Your age is", age)

name ="Nischal"
print("Helllo," + name + "!")

height = 1.75
print("Your height is", height)

isStudent = False
print("You are a student:", isStudent)

#basic arithmetic operations

a=10
b=5

print("Addition:", a+b)

print("Subtraction:", a-b)

print("Multiplication:", a*b)

print("Division:", a/b)

print("Modulus:", a%b)

#if else statement
num= int(input("Enter a number: "))
if num%2==0: print("The number is even.")
else: print("The number is odd.")

#for loop
for i in range(1,10):
    print(f"Hello {i}")

#while loop
count = 1
while count <= 5:
    print(count)
    count += 1

#function
def greet(name):
    print("Hello,", name + "!")

greet("Nischal")

#lists
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
fruits.append("orange")
print(fruits)

#tuples

coordinates = (10, 20)
print(coordinates)
print(coordinates[0])

#dictionaries
person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])
print(person.keys())
print(person.values())

#calculator basic
