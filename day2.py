#Try catch
try:
    a=9
    b=8
    print(isinstance(a, int))
    raise Exception()
except:
    print("An error occurred")
finally:
    print("This code will run anyways")

#Class and Object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Example usage
name = input("Enter your name: ")
age = int(input("Enter your age: "))
person = Person(name, age)
person.display()
            