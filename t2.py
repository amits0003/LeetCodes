class ElementNotFoundException:
    print("exception")


"This is a base class"
class Animal:
    """This is abstract method"""
    def SoundOfAnimal(self, animal_type, animal_name=None):
        pass
class Donkey(Animal):
    def SoundOfAnimal(self, animal_type, animal_name=None):
        print(" donkey : ", animal_type)
class Horse(Animal):
    def SoundOfAnimal(self, animal_type, animal_name=None):
        print(" Type 2 : ", animal_type)
        print("Horse : ", animal_name)


# obj1 = Horse()
# obj1.SoundOfAnimal("four legged", "Horse")
a = int(input("provide input"))
if a == 2:
    obj1 = Horse()
    obj1.SoundOfAnimal("Horse")
elif a == 3:
    obj1 = Donkey()
    obj1.SoundOfAnimal("Donkey")
else:
    print("None")



# def SumOfNumbers(a,b,c=None):
#     if c is None:
#         print(a+b)
#     else :
#         print(a+b+c)
#
# SumOfNumbers(2,3)
# SumOfNumbers(2,3, 4)