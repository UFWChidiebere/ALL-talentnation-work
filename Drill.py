# def solutio(numbers):
#     numbers = numbers.copy()

#     if len(numbers) == 0:
#         return
#     for i in range(len(numbers) - 1):
#         left = numbers[i]
#         right = numbers[i +1]

#         if left > right:
#             numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

#     print(numbers)

# solutio([1,4,2,6,8])

class Dog:
   species = "French Bulldog"

   def __init__(self, name):
     self.name = name

   def bark(self):
       return f"{self.name} says woof woof!"

jack = Dog("Jack")
jill = Dog("Jill")

print(jack.species)
print(jill.species)
print(jack.bark()) # Jack says woof woof!
print(jill.bark()) # Jill says woof woof!

print(jack.name, jack.species, jill.name, jill.species)
print(jill.name)