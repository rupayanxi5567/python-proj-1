# ======================================================== The Printing ======================================================


# print("hello")

# print("ooohohoho")

# print("pukuuuuuuuuuu")

# ====================================================== Membership operator ============================================================

stng_1 = "bambyyy"
# print("p" in stng_1 )
# print("y" in stng_1 )




# ====================================================== Bitwise operator ============================================================


x = 12
y = 13

# print(bin(x))    #returns the binary number
# print(bin(y))

# print(x&y)      #AND operation




# ====================================================== Data Types ============================================================


# my_sets = {1, 344, "buulu", 1, 'foty'}
# print(my_sets)



# ====================================================== Data Types ============================================================

# a = int(input("enter the number:"))

# if a%2 == 0:
#     print("it's an even number")
# elif a%2 != 0:
#     print("it's an odd number")
    
    
# ======================================= For Loop ========================================

#for i in range(start,end,jump):
    #print

# for n in range(5,400,10):
#     print(n)

# for i in range(1,11):
#     print( "2","*" , i ,  "is" , 2*i)
    
    
# ======================================= While Loop ========================================

# n=4
# while n<29:
#     print(n, "fotyy is mad")
#     n+=1



# ======================================= String Indexing ========================================

# word = "hello foty chondro ram"

# print(word[8])

# ======================================= String Slicing ========================================
# word = "hello foty chondro ram"
# print(word[0:10])
# print(word[-1::-1])  reverses your word


# ================================= String Slicing with gap ===============================

# word = "hello foty chondro ram"
# print(word[0::3])


# ================================= String Iteration ===============================
# word = "hello foty chondro ram"


# for i in word:
#     print(i)


# ================================= Reverse String Iteration-1 ===============================


# word = "hello foty chondro ram"
# word = word[-1::-1]

# length = len(word)
# print(length)

# for i in range(length):
#     print(word[i])
    
    
    # ================================= Reverse String Iteration-2 ===============================

# word = "hello foty chondro ram"

# length = len(word)
# print(length)

# for i in range(length-1,-1,-1):
#     print(word[i])



    # =============================Lower,upper,title character ==============================

# word = "Hello Foty chondro ram"
# new_word_lower = word.lower()
# new_word_upper = word.upper()
# new_word_title = word.title()
# new_word_capitalize = word.capitalize()
# print(new_word_capitalize)

# =============================== String Functions  find =============================== 

# word = "Hello Foty chondro ram"

# find_word = word.find("t")
# find_word_2 = word.find("ty")
# find_word_3 = word.find("o",5)  #find_word_3 = word.find("o", start from xth index )  
# print(find_word_3) 


# =============================== String Functions  Index =============================== 
# same as find




# =============================== String Functions  isalpha =============================== 

# word = "Hello Foty chondro ram"
# word_1 = "HelloFotychondroram"

# print(word.isalpha())
# print(word_1.isalpha())


# =============================== String Functions isdigit =============================== 

# word_num = "12345"
# word_num_dig = "abc12345"

# print(word_num.isdigit())
# print(word_num_dig.isdigit())

# =============================== String Functions alnum =============================== 

# word = "HelloFotychondroram"
# word_num = "Hello3444Fotychondroram"

# print(word.isalnum())
# print(word_num.isalnum())

# =============================== String Functions char =============================== 

# word = 165
# print(chr(word))


# =============================== String Functions ord =============================== 

# word = "B"
# print(ord(word))

# =============================== String Functions Format =============================== 

# word = "welcome {2} to the {0} of vs{1}".format("python", "code", "foty")
# print(word)


# =============================== Lists Slice ========================================== 

# l_1 = [1,2,64,32, "fotyy", 'buluu' , 699]

# sliced = l_1[0:6]
# print(sliced)

# sliced_1 = l_1[2:]
# print(sliced_1)

# sliced_2 = l_1[1:5:2]
# print(sliced_2)

# sliced_3 = l_1[-1::-1]
# print(sliced_3)


# =============================== Lists Iteration  ========================================== 

l_1 = [1,2,64,32, "fotyy", 'buluu' , 699]

# for n in l_1:
#     print(n)

# reverse

# length = len(l_1)

# for i in range(length-1,-1,-1):
#     print(l_1[i])


# =============================== Lists append-1  ========================================== 

# l = []

# for n in range(1,500):
#     l.append(n)
# print(l)


# shortcut

# p = [ x for x in range(1, 201)]
# print(p)

# shortcut with condition

# list = [x for x in range(1, 453) if x%5 == 0]
# print(list)


# shortcut with string

# name = "foty"
# listing = [ a for a in name  ]
# print(listing)



# =============================== Lists function - delete  ================================= 

# lists = [21, 423, 444, "fotu"]

# del lists[2]
# print(lists)



# =============================== Lists function - pop  ================================= 

# list_1 = [21, 423, 444, "fotu"]

# list_1.pop(1)
# print(list_1)

# print(list_1.pop(1))


# =============================== Lists function - remove  ================================= 


# list_1 = [21, 423, 444, "fotu"]

# list_1.remove("fotu")
# print(list_1)


# =============================== Lists function - clear  ================================= 

# list_2 = [21, 423, 444, "fotu"]

# list_2.clear()
# print(list_2)



# =============================== Lists function - update  ================================= 


# list_3 = [21, 423, 444, "fotu"]

# list_3[2] = "foty"
# print(list_3)



# =============================== Lists function - insert  ================================= 

# list_4 = [21, 423, 444, "fotu", "foty" ]

# list_4.insert(4, "fottuu")
# print(list_4)


# =============================== Lists append-2  ========================================== 

# list_5 = [21, 423, 444, "fotu"]

# list_5.append("foty")
# print(list_5)

# list_5.append(90)
# print(list_5)


# nested list append

# l_1 = [1,2,64,32, "fotyy", 'buluu' , 699]
# l_2 = [23,56]

# l_1.append(l_2)
# print(l_1)



# =============================== Lists extend  ========================================== 


# l_1 = [1,2,64,32, "fotyy", 'buluu' , 699]
# l_2 = [23,56]

# l_1.extend(l_2)
# print(l_1)


# =============================== Lists function - count ====================================== 

# list = [2, 343, 3445, 3445, "fottu", "foty", "foty", "fottu", "foty", 3445]

# print(list.count(3445))
# print(list.count("fottu"))


# =============================== Lists function - max ====================================== 

# list = [2, 343, 3445, 3445, 3445]

# print(max(list))

# list_1 = [ "fottu", "foty", "foty", "fottu", "foty"]
# print(max(list_1))


# =============================== Lists function - min ====================================== 

# list = [2, 343, 3445, 3445, 3445]

# print(min(list))

# list_1 = [ "fottu", "foty", "foty", "fottu", "foty"]
# print(min(list_1))



# =============================== Lists function - sort ====================================== 

# lists = [2, 343, 3445455555555555555555555, 3445333434, 34454]

# lists.sort()
# print(lists)



# ============================== Lists function - reverse ====================================== 

# lists = [2, 343, 3445455555555555555555555, 3445333434, 34454]

# lists.reverse()
# print(lists)


# ============================== Lists function - index ====================================== 

# lists = [2, 343, 3445455555555555555555555, 3445333434, 34454]

# print(lists.index(34454))



# ============================== Lists function - zip ====================================== 


# list_1 = [ "fottu", "foty", "foty", "fottu", "foty"]

# lists = [2, 343, 3445333434, 34454]

# for x,y in zip(list_1,lists):
#     print(x,y)



# ============================== Lists function - split-1 ====================================== 

# line = input("enter the line: ")

# listed = line.split()

# print(listed)



# ============================== Lists function - split-2 ====================================== 

# e_l = []

# for a in range(1,6):
#     n = input("enter the name-1: ")
#     e_l.append(n)
# print(e_l)


# ============================== Stacks Operation ====================================== 

# list = []

# while True:
#     took_input = int(input(
#         '''
#     1. push
#     2. pop
#     3. peek
#     4. display
#     5. exit
#     enter any number
# '''
#     ))
#     if took_input == 1:
#         data_val_push = input("enter the value: ")
#         list.append(data_val_push)
#         print( "adding successful, your disired list is ", list)
#     elif took_input == 2:
#         if list == []:
#             print("Your list is empty, please enter any value at first to pop that")
#         else:
#             pooped = list.pop()
#             print("popped the element", pooped)
#             print( "popping successful, your disired list is ", list)
#     elif took_input == 3:
#         if list == []:
#             print("Your list is empty, please enter any value at first to peek that")
#         else:
#             peeking = list[-1]
#             print("peeked the last element", peeking)
#     elif took_input == 4:
#         print( "your disired list is ", list)
#     elif took_input == 5:
#         break;
    
    
    # ============================== Queue Operation ====================================== 

# list = []

# while True:
#     took_input = int(input(
#         '''
#     1. push
#     2. pop first
#     3. front element
#     4. last element
#     5. display stack
#     6. exit
#     enter any number
# '''
#     ))
#     if took_input == 1:
#         data_val_push = input("enter the value: ")
#         list.append(data_val_push)
#         print( "adding successful, your disired list is ", list)
#     elif took_input == 2:
#         if list == []:
#             print("Your list is empty, please enter any value at first to pop that")
#         else:
#             del list[0]
#             print( "popping successful, your disired list is ", list)
#     elif took_input == 3:
#         if list == []:
#             print("Your list is empty, please enter any value at first to peek that")
#         else:
#             peeking = list[0]
#             print("peeked the first element", peeking)
#     elif took_input == 4:
#         if list == []:
#             print("Your list is empty, please enter any value at first to peek that")
#         else:
#             peeking = list[-1]
#             print("peeked the last element", peeking)
#     elif took_input == 5:
#         print( "your disired list is ", list)
#     elif took_input == 6:
#         break;

    # =================================== Dictionary ====================================== 

# foty_dict = {
#     "name": "foty chondro",
#     "age": 18,
#     "gender": "female",
#     "address": "kathmandu",
#     "college": "iitm"
# }
# print(foty_dict["age"])

# list_of_dict = foty_dict["address"] 
# print(list_of_dict)

#     # ================================ for loop in Dictionary ====================================== 

# foty_dict = {
#     "name": "foty chondro",
#     "age": 18,
#     "gender": "female",
#     "address": "kathmandu",
#     "college": "iitm"
# }

# for x in foty_dict:
#     print(x, foty_dict[x]  )



#     # ============================= Dictionary Functions-get ====================================== 

# foty_dict = {
#     "name": "foty chondro",
#     "age": 18,
#     "gender": "female",
#     "address": "kathmandu",
#     "college": "iitm"
# }

# getting = foty_dict.get("name")
# print(getting)



#     # ====================== Dictionary Functions-get Keys, values =========================== 

# foty_dict = {
#     "name": "foty chondro",
#     "age": 18,
#     "gender": "female",
#     "address": "kathmandu",
#     "college": "iitm"
# }

# for x in foty_dict.keys():
#     print(x)
# for y in foty_dict.values():
#     print(y)

#     # ====================== Dictionary Functions- items =========================== 

# foty_dict = {
#     "name": "foty chondro",
#     "age": 18,
#     "gender": "female",
#     "address": "kathmandu",
#     "college": "iitm"
# }

# for a,b in foty_dict.items():
#     print(a,b)


#     # ====================== Dictionary Functions- items =========================== 

# foty_dict = {
#     "name": "foty chondro",
#     "age": 18,
#     "gender": "female",
#     "address": "kathmandu",
#     "college": "iitm"
# }

# del foty_dict["address"]
# print(foty_dict)



#     # ====================== Dictionary Functions- pop =========================== 

# foty_dict = {
#     "name": "foty chondro",
#     "age": 18,
#     "gender": "female",
#     "address": "kathmandu",
#     "college": "iitm"
# }

# foty_dict.pop("address")
# print(foty_dict)



#     # ====================== Dictionary Functions- dict =========================== 

# foty_dict = dict(name="foty chondro", age=18, gender="female", address="siliguri", college="iitm")

# print(foty_dict)


#     # ====================== Dictionary Functions- update =========================== 

# foty_dict = {
#     "name": "foty chondro",
#     "age": 18,
#     "gender": "female",
#     "address": "kathmandu",
#     "college": "iitm"
# }

# foty_dict.update({"house": "new" })
# print(foty_dict)

# foty_dict.update({"address": "siliguti" })
# print(foty_dict)



#     # ====================== Dictionary Functions- insert =========================== 

# foty_dict = {
#     "name": "foty chondro",
#     "age": 18,
#     "gender": "female",
#     "address": "kathmandu",
#     "college": "iitm"
# }

# foty_dict["house"] = "flat"
# print(foty_dict)


#     # ====================== Dictionary Functions- clear =========================== 

# foty_dict = {
#     "name": "foty chondro",
#     "age": 18,
#     "gender": "female",
#     "address": "kathmandu",
#     "college": "iitm"
# }

# foty_dict.clear()
# print(foty_dict)


#     # ====================== Dictionary Functions- nesting =========================== 

# foty_dict = {
#     "name": {"nick": "fotu", "last": "chondro", "another": "mum"  } ,
#     "age": {"new": 18, "old": 17, "another_will_be": 19 },
#     "gender": {"my_gender":"male", "her_gender": "female" },
#     "address": {"street": "pipleine", "city": "siliguri", "state": "west bengal"} ,
#     "college": {"online": "IITM", "offline": "mahila college" }  
# }

# her_gender_get = foty_dict["gender"]["her_gender"]
# print(her_gender_get)

    # ====================== Dictionary Functions- loops in nesting =========================== 

# foty_dict = {
#     "name": {"nick": "fotu", "last": "chondro", "another": "mum"  } ,
#     "age": {"new": 18, "old": 17, "another_will_be": 19 },
#     "gender": {"my_gender":"male", "her_gender": "female" },
#     "address": {"street": "pipleine", "city": "siliguri", "state": "west bengal"} ,
#     "college": {"online": "IITM", "offline": "mahila college" }  
# }

# for a,b in foty_dict.items():
#     print(a,b)
#     for p,q in b.items():
#         print(p,q)


#     # ================================ Tuple =========================================== 

# tups = ("sonta", "ouu", 121, 3879342879, "numbers" )

# tups_get = tups[2]
# print(tups_get)


#     # =========================== Tuple functions - get ====================================== 

# tups = ("sonta", "ouu", 121, 3879342879, "numbers" )

# for x in range(len(tups)):
#     print(tups[x])
    
    
    #shortcut

# for y in tups:
#     print(y)



#     # ======================== Tuple functions - min,max ====================================== 

# tups = (121, 3879342879 )

# print(max(tups))
# print(min(tups))


#     # ======================== Tuple functions - counting =============================== 

# tups = ("sonta", "ouu", "sonta", 121, 3879342879, "numbers" )

# counting = tups.count("sonta")
# print(counting)


#     # ======================== Tuple functions - index ==================================== 

# tups = ("sonta", "ouu", "sonta", 121, 3879342879, "numbers" )

# indexing = tups.index("numbers")
# print(indexing)



#     # ======================== Tuple functions - sum ==================================== 

# tups = (121, 3879342879)

# summin = sum(tups)
# print(summin)


#     # ==================================== Set ==================================== 

# setts = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# print(setts)

# for x in setts:
#     print(x)


# ============================== Sets functions-set ==================================== 

# listing = [12,2232,5435]

# setting = set(listing)
# print(setting)



# # =========================== Sets functions-remove,discard ============================= 

# setting = {12,2232,5435}

# setting.remove(2232)
# print(setting)

# setting.discard(2232)
# print(setting)


# # =========================== Sets functions-pop ==========================

# setting = {12,2232,5435}
# setting.pop()
# print(setting)


# # =========================== Sets functions-clear ==========================

# setting = {12,2232,5435}
# setting.clear()
# print(setting)


# # =========================== Sets functions-add ==========================

# setting = {12,2232,5435}
# setting.add(45)
# print(setting)



# # =========================== Sets functions-update ==========================
# listing = [221,12, 33334,"fotyy"]
# setting = {12,2232,5435}
# setting.update(listing)
# print(setting)


# =========================================functions =============================================
# def square_it(x):
#     return x*x
# print(square_it(4))
    
    
# ========================================= math functions =============================================

# import math

# print(math.ceil(2.2))
# print(math.floor(2.9))
# print(math.fabs(-2.6))
# print(math.factorial(57))

# lists = [23,43]
# print(math.fsum(lists))

# print(math.sqrt(26))

    
# ====================================== random functions =============================================

# import random

# print(random.randint(1,100544444333333333222))
# print(random.randrange(1,10054444433333222))

# listing = [1,2,3,4,5,6,7,8]
# print(random.choice(listing))

# print(random.random()*100)

# listing = [1,2,3,4,5,6,7,8]
# random.shuffle(listing)
# print(listing)

# print(random.uniform(1,100))



# ====================================== random functions =============================================
# import datetime

# print(datetime.datetime.now())
# print(datetime.datetime(2025,11,3))

# x = datetime.datetime.now()
# print(x.strftime("%Y"))
# print(x.strftime("%b"))




# ====================================== Number Guessing Game  ========================================
# import math,random

# computer_input = random.randint(1,100)
# chances = []

# for x in range(10):
#     user_input = int(input("Enter the number: "))
#     if user_input == computer_input:
#         print("Congratulation, You win the match!")
#         chances.append(user_input)
#         print("Your chances are ", chances)
#         break;
#     elif user_input < computer_input:
#         print("Your number is too low, try again, chances left ", 9-len(chances) )
#         chances.append(user_input)
#         print("Your chances are ", chances)
#     elif user_input > computer_input:
#         chances.append(user_input)
#         print("Your chances are ", chances)
#         print("Your number is too high, try again, chances left ", 9-len(chances) )
# print("game ended your guesses were", chances )
# print("The actual number was ", computer_input)


# ============================= rock, paper, scissors game  ======================================== 
# import math,random

# list_of_choice = ["rock", "scissor", "paper"]


# while True:
#     c_count = 0
#     u_count = 0
#     user_choice = int(input('''
# Game starts
# 1 Yes
# 2 No | Exit
# '''    
#     ))
#     if user_choice == 1:
#         for x in range(1, 6):
#             user_input = int(input('''
# Choose your move 
# 1 Rock
# 2 Scissor
# 3 Paper


# '''))
#             if user_input == 1:
#                 u_choice = "rock"

#             elif user_input == 2:
#                 u_choice = "scissor"

#             elif user_input == 3:
#                 u_choice = "paper"

#             comp_choice = random.choice(list_of_choice)

#             if u_choice == comp_choice:
#                 print("Computer choice is", comp_choice, "and your choice is", u_choice)
#                 print("Draw the round" , x)
#                 u_count+=1
#                 c_count+=1
#                 print("Your score is", u_count, "and computer score is", c_count) 
#             elif ( u_choice=="paper" and comp_choice== "rock" ) or ( u_choice == "rock" and comp_choice == "scissor" ) or ( u_choice == "scissor" and comp_choice == "paper"):
#                 print("Computer choice is", comp_choice, "and your choice is", u_choice)
#                 print("You win round", x)
#                 u_count+=1
#                 print("Your score is", u_count, "and computer score is", c_count) 
#             elif ( u_choice == "paper" and comp_choice == "scissor" ) or ( u_choice == "rock" and comp_choice == "paper" ) or ( u_choice == "scissor" and comp_choice == "rock"):
#                 print("Computer choice is", comp_choice, "and your choice is", u_choice)
#                 print("You lose round", x)
#                 c_count+=1
#                 print("Your score is", u_count, "and computer score is", c_count) 
#         if u_count > c_count:
#             print("You win the game")
#             print("Try again?")
#         elif u_count < c_count:
#             print("You lose the game")
#             print("Try again?")
#         elif u_count == c_count:
#             print("Draw the game")
#             print("Try again?")
        
            
#     elif user_choice == 2:
#         break;
    
#     # ================================== JSON  ======================================== 

# import json
# fotyr_dict = {
#     "name": "Fotyr",
#     "age": 19,
#     "house_id": "ouu"
# } 

# creating_json = json.dumps(fotyr_dict)        #from dict to JSON
# print(creating_json)




    # ================================== JSON  ======================================== 

# import json

# fotyr_dict = '[{"name": "Fotyr", "age": 19, "house_id": "ouu"}]'

# loading_json = json.loads(fotyr_dict)   #from JSON to dict
# print(type(loading_json))



    # ================================== OOPS-1  ======================================== 

# class demo_going:
#     fotyr_name = "bambyy"
    
# the_obj = demo_going()
# print(the_obj.fotyr_name)



# class maths_class:
#     a = "fotu"
#     def multi(self):
#         print(2*4)

# maths_class_obj = maths_class()
# maths_class_obj.multi()



    # ================================== OOPS-2  ======================================== 

# class checking:
#     a = 44
#     def name_checking(self):
#         self.c = self.a*self.a
#         print(self.c)
#     def foty_name(self):
#         print("ore o sonta bby dekha tor nongra pasuu")
#     def param_fnc_add(self, x,y):
#         print(x+y)
                
# checking_obj = checking()

# checking_obj.name_checking()
# checking_obj.foty_name()
# checking_obj.param_fnc_add(20,30)



#constructor

# class construc_tut:
#     def __init__(self):
#         print("fotyr constructor")

# construc_tut_obj = construc_tut()



    # ================================== OOPS-3  ======================================== 

# class A:
#     def A(self):
#         print("ouuu A")

# class B(A):                                 # now class A has gone inside class B
#     def B(self):
#         print("ouuu B")
        
# obj_b = B()

# obj_b.A()
# obj_b.B()



# multi inheritance

# class A:
#     def A(self):
#         print("ouuu A")

# class B(A):                                 # now class A has gone inside class B
#     def B(self):
#         print("ouuu B")
        

# class C(B):                                 # now class A,B has gone inside class C
#     def C(self):                            # or you can also use C(A,B) instead of line 1046 B(A)
#         print("ouuu C")
        
# obj_c = C()

# obj_c.A()
# obj_c.B()
# obj_c.C()


    # ============================== OOPS-3 [encapsulation, getter-setter] ======================= 
# class students:
#     def __init__(self):
#         self.__name = ""              __name indicates pvt variable
#     def getter_name(self):
#         return self.__name
#     def setter_name(self, naming):
#         self.__name = naming

# students_obj = students()

# students_obj.setter_name("fotkii")
# the_name = students_obj.getter_name()
# print(the_name)
        
        
        
# ============================== OOPS-4 [encapsulation, getter-setter] ======================= 

# class students_name():
#     __nameing = "fottu"
#     def __init__(self):
#         print(self.__nameing)

# obj_student_name = students_name()


# pvt fnc

# class students_mms():
#     def __init__(self):
#         self.__theMms()
#     def __theMms(self):
#         print("studeent's mms got licked")

# obj_std_mms = students_mms()


# ===================================== OOPS-5 [Polymorphism] ============================== 

# overloading

# class bby:
#     def display_greeting(self):
#         print("I love you!")

# bby_obj = bby()
# bby_obj.display_greeting("fomtuuu")



# overwriting

# class bby:
#     def display_greeting(self):
#         print("I love you bby!")

# class bbt(bby):                         # bby got inherited insdie this one
#     def display_greeting(self):
#         super().display_greeting()
#         print("I love you bbt!")
        
# bbt_obj = bbt()
# bbt_obj.display_greeting()



# =============================== OOPS-5 [overloading and overriding] ============================== 

# overloading

# class quad:
#     def find_area(self, h = None, k = None):
#         if (h != None and k != None):
#             print("The area of the rectangle is ", h*k  )
#         elif k == None and h!= None:
#             print("The area of the square is", h*h )
#         else:
#             print("Please give proper value")
        
# quad_obj = quad()

# quad_obj.find_area(21, 45)
# quad_obj.find_area(21)
# quad_obj.find_area(32, 0)


# overriding

# class A:
#     def show_class(self):
#         print("I am in class A")

# class B(A):
#     def show_class(self):
#         print("I am in class B")
        
# obj_b = B()

# obj_b.show_class()


# =============================== OOPS-6 BMW Renting Project ============================== 

class bmw_shop:
    def __init__(self, stock):
        self.stock = stock

    def display_bmw(self):
        print("Total BMW available", self.stock)
    def renting(self, quan):
        
        if quan < 1:
            print("BMW quantity can't be zero or negetive")
        elif quan > self.stock:
            print("Can't rent more than stocks", self.stock)
        else:
            print("Thanks for ordering, your total price is ", quan*1000 )
            print("Stocks remaining:", self.stock-quan )
            
while True:
    bmw_shop_obj = bmw_shop(2000)
    user_choice = int(input( '''
1. Display Stocks
2. Rent BMW
3. Exit
'''))
    
    if user_choice == 1:
        bmw_shop_obj.display_bmw()
    elif user_choice == 2:
        user_value = int(input("Enter the Quantity :-- "))
        bmw_shop_obj.renting(user_value)
    else:
        break;