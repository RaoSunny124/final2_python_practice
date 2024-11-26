# print("Rao \"Hassan\" \'Ali\'")
# print("Hassan\t Ashraf")
# print("Hassan\nAshraf")
# print("Hassan\\Ashraf")
# print("Hassan \"Ashraf\"")


#input function
# age = print(type(int(input('Your age is:'))))

#String
# anything indside a inverted commas is considered as a String.
# name = "My name is Hassan"
# print(name)
# for x , y  in enumerate(name):
#     print(x , y)
# # syntax[start , end or -1 , step]
# print(name[11 : 17 : 2]) 
# print(name[:: 2])   
# print(name[:: -1])   

# name = "My name is Hassan"
# print(name.split())
# print(name.startswith('M'))
# print(name.center(50 , 'M'))
# print(name.capitalize())
# print(name.title() )

#if\else\elif statement
# marks = int(input('marks:'))
# # age = int(input('age:'))
# if marks <= 80:
#     print('Good marks')
#     age = int(input('age:'))
#     if age <= 20:
#         print('eligible for driving.')
#     else:
#         print('not eligible.')    
# elif marks <= 50:
#     print('Satisfactory marks')    
# elif marks <= 33:
#     print('passing marks') 
# else:
#     ('fail')       

name = "Hassan"
# for x in name:
    # print(x , end="")

# for x in range(2 , 21 , 2):
#     print(x)                                        


#While
# score = 0
# while score < 5:
#     print(score)
#     score = score + 1

#control statement
# score = 0
# while score < 5:
#     print(score)
#     score = score + 1
#     if score == 3:
#         break


#function
# def even_odd():    #function decleration
#         user_input = int(input('Number:'))
#         if user_input%2 == 0:
#             print('even')
#         else:
#             print ('odd')   

# even_odd()   #function calling

# def even_odd(x):
#     """This function is check for even or odd"""   
#     if x%2 == 0:
#             print('even')
#     else:
#             print ('odd')   

# for x in range(1 , 4):
#     even_odd(int(input('Number:'))) 

# print(even_odd.__doc__)


# non-primitive: it can store multi type value
# li = [1 ,2 ,3, 4, 5, 6, 7 , 8, 9 , True]
# li2 = [2,1,4,3,2,5]
# li.append(10)
# print(li)
# li.insert(2 , 5)
# print(li)
# li.pop(2)
# print(li)
# li2.sort()
# print(li2)
# li.reverse()
# print(li)
# li.extend([11,12])
# print(li)


#tuple
# tu = (1 ,2 ,3, 4 , 'Hassan')
# print(tu)
# print(tu[0 : 6 : 2])
# for x ,y in enumerate(tu):
#     print(x ,y)


#dictionary
# dic = {'a' : 'Hassan' , 'b' : 19 , 'c' : 'inter'}
# print(dic['a'])
# for x , y in dic.items():
#     print(f'{x} : {y}')
# print(dic.items())
# print(dic.get('f'))
# print(dic.keys())
# print(dic.setdefault('e' , "ALi"))
# print(dic)
# print(dic.update({'e' : 'HUzaifa'})) 
# print(dic)   
# print(dic.popitem())


# li = [2,1,4,3,2,5]
# dic = {}
# for x , y in enumerate(li):
#     dic[x] = y
# print(dic) 

# li = []
# name = 'Hassan'
# for x in enumerate(name):
#     li.append(x)
# print(li)  


#error handling
# try:
    # age = int(input('age:'))
    #   print(age)
#     print(int(input('age:')))
# except Exception as e:
#     print('Please enter a number , it is error.' , e)    
# else:
#     ('no error')
# finally:
#     print('am must run.')



#OOP
# inheritance
# class Grand_pa():
#     def G_guide(self):
#         print('G_papa is guide.')
#     def G_care(self):
#         print('G_papa is caring.')     
# class Father():
#     def guide(self):
#         print('Father is guiding.')
#     def care(self):
#         print('Father is caring.')

# class Mother(Father):
#     def cook(self):
#         print('Mother is cooking.')
#     def protect(self):
#         print('Mother is protecting.')        


# class Children(Mother):
#     def __init__ (self , name , age , height):
#         self.name = name
#         self.age = age
#         self.height = height
#     def eat(self , meal):
#         print(f'Child is eating {meal}.')   
#     def play(self):
#         print('Child is playing.')       

# # class Children2(Mother):
# #     def __init__ (self , name , age , height):
# #         self.name = name
# #         self.age = age
# #         self.height = height
# #     def eat2(self , meal):
# #         print(f'Child2 is eating {meal}.')   
# #     def play2(self):
# #         print('Child2 is plying.')


# c1 = Children('Hassan' , 19 , 5.8)
# print(c1.name)
# print(c1.age)
# print(c1.height)
# c1.eat('baby food')
# c1.play()
# c1.care()
# c1.guide()
# c1.protect()
# c1.cook()
# c1.G_care()
# c1.G_guide()

# print()

# c2 = Children(age= 18 , height=5.6 , name= 'Ali')
# print(c2.name)
# print(c2.age)
# print(c2.height)
# c2.eat('potato')
# c2.play()
# c2.care()
# c2.guide()
# c2.protect()
# c2.cook()
# c2.G_care()
# c2.G_guide()


#Encapsulation

# class Human():
#     def __init__ (self , name , age , height):
#         self.__name = name
#         self.__age = age
#         self.__height = height
#     def eat(self , meal):
#         print(f'{self.__name} is eating {meal}.')   
#     def sleep(self):
#         print(f'{self.__name} is sleeping.')
#     # def get(self):
#     #     return self.__name , self.__age , self.__height    

# H1 = Human('Mirha' , 15 , 5.2)

# # print(H1.__name)
# # print(H1.__age)
# # print(H1.__height) 
# H1.eat('Pulao')
# H1.sleep()       
# # print(H1.get())



#polymorphism

# class Cal():
#     def add(self , *a):
#         return sum(a)


# c1 = Cal()
# print(c1.add(2 ,4))



# class Cal():
#     def add(self , a , b):
#         return a+b       
#     def add(self , a ,b ,c):
#         return a+b+c    



# A1 = Cal()
# print(A1.add(2 , 2 , 4 ))














#Abstraction




