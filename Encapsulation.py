class Person():
    def __init__(self , name , age):
        self.__name = name 
        self.__age = age
    def admin(self):
        return self._name , self._age


p1 = Person('hassan' , 19)

# print(Person._name)
# print(Person._age)
# print(Person.admin())

print()