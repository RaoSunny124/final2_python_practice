# class Father():
#     def guide(self):
#         print('parents guiding')
#     def care(self):
#         print('father caring')
# class Mother(Father): 
#     def cook(self):
#         print('mother cooking')
#     def protect(self):
#         print('mother protecting')           
# class Children(Mother): 
#     def play(self):
#         print('children playing')
#     def eat(self):
#         print('children eating')                   

# C1 = Children()
# C1.guide()
# m1 = Mother()
# m1.care()

class Father():
    def guide(self):
        print('parents guiding')
    def care(self):
        print('father caring')
class Mother(Father): 
    def cook(self):
        print('mother cooking')
    def protect(self):
        print('mother protecting')           
class Children1(Mother): 
    def play(self):
        print('children playing')
    def eat(self):
        print('children eating') 
class Children2(Mother): 
    def play2(self):
        print('children playing')
    def eat2(self):
        print('children eating')                           
c1 = Children1

c2 = Children2
