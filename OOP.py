# class Dog:
#     breed = 'german'
#     colour = 'black'
#     age = 3


#     def bark(self):
#         print('dog barks')
#     def run(self):
#         print('dog run')
#     def sleep(self):
#         print('dog sleep')    


# D1 = Dog()

# print(D1.breed)
# print(D1.colour)
# print(D1.age)


# D1.bark()
# D1.run()
# D1.sleep()



# class Human:
#     name = 'Hassan'    #attribute , detail #static
#     height = 5.7
#     age = 19


#     def eat(self):     #method , action , function
#         print('i am eat')
#     def talk(self):
#         print('human talk')
#     def sleep(self):
#         print('human sleep')    


# H1 = Human()  #Object making

# print(H1.name)
# print(H1.height)
# print(H1.age)


# H1.eat()
# H1.talk()
# H1.sleep()



# li = list([1 ,2 , 3])
# print(li)

# li.clear()
# print(li)



# class Human:
#     def __init__(self , name , height , age):
#         self.name = name    
#         self.height = height
#         self.age = age


#     def eat(self , meal):   
#         print(meal , 'is eating.')
#     def talk(self):
#         print('human talk')
#     def sleep(self):
#         print('human sleep')    


# H1 = Human('Hassan' , 5.7 , 19) 
# H2 = Human('ALi' , 5.6 , 18)

# print(H1.age)
# print(H1.height)

# # H1.eat()

# print()
# print(H2.age)

# H2.eat ('ali')


# class Cat():
#     def __init__(self , breed , colour , age):
#         self.breed = breed
#         self.colour = colour
#         self.age = age

#     def eat(self , cat_name):
#         print(cat_name , 'is eating')    
#     def walk(self , cat_name):
#         print(cat_name , 'is walking')
#     def sleep(self , cat_name):
#         print(cat_name , 'is sleeping')       

# C1 = Cat( colour = 'white' , breed='perssion' ,  age=3)    

# print(C1.breed)
# print(C1.colour)
# print(C1.age)
# print()
# C1.eat('mano')
# C1.walk('mano')
# C1.sleep('mano')

# print()
# C2 = Cat(age=5 , breed='african' , colour='black')
# print(C2.breed)
# print(C2.colour)
# print(C2.age)
# print()
# C2.eat('Kity')
# C2.walk('Kity')
# C2.sleep('Kity')


# user_input = input('\033[34mEnter your name:\033[0m')   # make text blue....
# print(user_input)


# user_input = input('\033[1;3mEnter your name:\033[0m')   # make text bold and italics....
# print(user_input)

# \033[34m text  \033[0m
# For bold and italics:
# \033[1;3m  text  \033[0m
