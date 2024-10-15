# Qn 24
import math

def compute_hypothenuse(length, breath):
    hyp_squared = (length ** 2) + (breath ** 2)
    hyp = math.sqrt(hyp_squared)
    return hyp


x = compute_hypothenuse(3, 4)
print(x)

# Qn 30
def addition(N):
    for numbers in range(1, N + 1):
        sum = numbers + numbers
        print(f"{numbers} + {numbers} = {sum}")

addition(10)

# Qn 31 
def multiple(N):
    for nos in range(1, N + 1):           # for loop
        product = nos * nos
        print(f"{nos} x {nos} = {product}")

multiple(10)

# Qn 32 
def numbers(N):                 
    result = " - ".join((str(nos)) for nos in range(1, 1 + N))  # for loop
    print(result)

numbers(10)
"""
def nums(N):
    i = 1
    while i < (N + 1):
        print(i 
        if i == 10:
            break
"""

# Qn 32 
def nums(N):
    result = " : ".join((str(nums)) for nums in range(1, 1 + N))
    print(result)

nums(10)

# Qn 33
def nums():
    numbers = [12, 14, 16, 18, 20]
    result = ", ".join((str(nums)) for nums in numbers)
    print(result, end=".")

nums()

def nums(N):
    numbers = []
    
    for num in range(12, N + 1, 2):
        numbers.append(str(num))
        if num == N:
            break

    result = ", ".join(numbers)
    print(result, end=".")

nums(20)

# Qn 33
def nums(N):
    numbers = []

    for num in range(1, int((N - 1) / 0.2) + 1):
        i = round(1.0 + (num * 0.2), 2)
        numbers.append(str(i))
        if i >= N:
            break

    result = " * ".join(numbers)
    print(result, end=".")

nums(4.0)

# Qn 33
def nums(N):
    nos = []

    for i in range(1, N + 1, 2):
        nos.append(str(i))
        if i == N:
            break

    result = "; ".join(nos)
    print(result, end=".")

nums(9)

# Qn 34
def num_list(N):
    for num in range(N + 1):    # For loop repeats number from 0 to N (loop variable is num)
            result = "".join(str(num) for num in range(0, num + 1, 2)) 
            # Inner For Loop and Join: Within the outer loop, it defines a string by joining the
            # string representation of even numbers from 0 to the current value of 'num' 
            # using "" (empty string) as the separator 
            print(result)

num_list(20)

# 35 
"""
def num_fn(N):
    for num in range(1, N + 1):
        result = "".join(str(numbers))
        qn_mk = "".join([(numbers + "?") for numbers in range(1, num +1)])
        print(result + qn_mk)

num_fn(6)
# This code is wrong because you dont need to join anything
"""

def num_fn(N):
    for num in range(1, N + 1):  # For loop repeats numbers from 1 to N + 1. 
        result = str(num) + "?" * (num - 1)   
        print(result)

num_fn(6)

def num_fn():
    N = int(input("Enter a number (1-9): ")) # alternatively: def num_fn(N):
    for num in range(1, N + 1):              #   for num in range(1, N + 1)
        result = str(num)                    #      result = str(num) + ("?" * (num - 1))
        qn_mk = "?" * (num)                  #      print(result)
        print(result + qn_mk)

num_fn()

# Qn 35
def num_fn():
    N = input("Enter a number (1-9): ") 
    for num in range(N, 0, -1):        # (1, N + 1) = (1, N + 1, 1)
        result = str(num)
        minus = "-" * (num)

        print(minus + result)

num_fn()

# Qn 36
def int_fn():
    min_value = input("Enter the minimum integer: ")
    max_value = input("Enter the maximum integer: ")

    int_list = ["Number"]
    sign_list = ["Sign"]
    par_list = ["Parity"]

    for num in range(int(min_value), int(max_value) + 1):
        int_list.append(num)
        
       # sign_list = [] sign_list should be initialized outside the loop to 
       #                store the sign information for each number.

        if num < 0:
            sign_list.append("negative")
        elif num > 0:
            sign_list.append("positive")
        else:
            sign_list.append("zero")

        if num % 2 == 0:
            par_list.append("Even")
        else:
            par_list.append("Odd")

    for value, sign, parity in zip(int_list, sign_list, par_list):
        print("{:<6}   {:<10}   {:<6}".format(value, sign, parity))

int_fn()

# Qn 37
def num_list(N):
    numbers = []
    i = 0             # i needs to be initialized first
    while i < int(N):      
        i += 1       # same as i = i + 1 loops numbers from 1 to N 
        numbers.append(str(i))


    result = " : ".join(numbers)   
    print(result)

num_list(10)

# output = 1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9 : 10

def num_list(N):
    result = ""
    i = 0
    while i < N:           # runs through numbers from 1 to N to check if number is < N
        i += 1             # while the number is < N, i + 1 will be added to result
        result += str(i)   # in a string format     
        if i < N:          # and if i < N adds " : " to result before looping to the next number
            result += " : "

    print(result)

num_list(10)

# output = 1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9 : 10



def num_list(N):
    numbers = []
    i = 0             # i needs to be initialized first
    while i < int(N):      
        i += 2       # same as i = i + 1 loops numbers from 1 to N 
        numbers.append(str(i))


    result = " * ".join(numbers)   
    print(result, end=".")

num_list(10)

def num_list(N):
    numbers = []
    i = -1
    while i < N - 1:
        i += 2
        numbers.append(str(i))

    result = " ; ".join(numbers)
    print(result, end=".")

num_list(10)

# Qn 38 
def equations(N):
    
    numbers = []
    signs = []
    eq_signs = []
    sums = []

    i = 0
    while i < N + 1:
        i += 2
        numbers.append(i)

        sums1 = i + i
        sums.append(sums1)

        sign1 = 0
        eq_signs1 = 0
            
        if i < N + 1:
            sign1 += 1
            signs2 = str(sign1 * "+")
            signs.append(signs2)

            eq_signs1 += 1
            eq_signs2 = str(eq_signs1 * "=")
            eq_signs.append(eq_signs2)
            


    for number, sign, number, eq_sign, sum in zip(numbers, signs, numbers, eq_signs, sums):
        print("{:>3} {:^1} {:>3} {:^1} {:>3}".format(number, sign, number, eq_sign, sum))

def equations(N):
    i = 0
    while i < N:
        i += 2
        number = i
        sign = "+"
        eq_sign = "="
        sums = i + i

        print("{:>3} {:^1} {:>3} {:^1} {:>3}".format(number, sign, number, eq_sign, sums))

equations(10)

    
equations(10)

# Qn 39
def function1():

    no_even = 0
    no_odd = 0
    no_neg = 0
    no_pos = 0
    zero = 0
    integer = []
    while True:
        user_input = input("Enter an integer or q to quit: ")
        if user_input == "q":
            break
        else:
            integer.append(int(user_input))
        no_integers = len(integer)

        number = int(user_input)

        if number % 2 == 0:
            no_even += 1

        else:
            no_odd += 1
        

        if number > 0:
            no_pos += 1
        elif number == 0:
            zero += 1
        else:
            no_neg += 1
        
        sum_nos = sum(integer)
    
    txt3 ="There are {0} odd numbers. There are {1} positive numbers. There are {2} negative numbers"
    print("Summary information: ")
    print(f"You have entered {no_integers} integers. The sum of these numbers is {sum_nos} . There are {no_even} even numbers.")
    print(txt3.format(no_odd, no_pos, no_neg))        

function1()

# Qn 40
def next_number(X):
    
    sequence = [X]

    if X % 2 == 0:
        result = 3 * X + 1
        return result
    else:
        result = 2 * X + 2
        return result
    

first_integer = 1
result = next_number(first_integer)
print(f"For initial integer, {first_integer}, the next number is {result}.")

# Qn 41 
def next_number():
    
    sequence = []
    step_no = -1
    step = "Step"
    colon = ":"
    
    X = int(input("Enter the initial number: "))
    while X < 50:

        if X % 2 == 0:
            result = 3 * X + 1
               
        else:
            result = 2 * X + 2
        step_no += 1
        sequence.append(result)
                         
    print("Sequence: ") 
    for i in range(-1, step_no):
        print("{:<4}  {:^1}{:^1}  {:>2}".format(step, i, colon, sequence))
    print("... this goes until the number becomes greater than 1 million then stops...")   
        
       
next_number()


def next_number():
    
    step = "Step"
    colon = ":"
    
    X = int(input("Enter the initial number: "))
    step_no = -1
    sequence = [X]
    
    while X > 0  and step_no < 3:
        if X % 2 == 0:
            result = 3 * X + 1
        else:
            result = 2 * X + 2
        
        step_no += 1
        sequence.append(result)
        X = result          # without this line, X will never change and there wont be a loop

    print("Sequence:")
    for i in range(0, step_no + 1):
        print("{:<4}  {:^1}{:^1}  {:>2}".format(step, i, colon, sequence[i]))
    print("... this goes until the number becomes greater than or equal to 50 then stops.")

next_number()

# Qn 42
# i
list = [1,2,3,4,1,2,3,4] 
# ii
list.append(2000)
# iii
del list[0]
# iv
list[7] = 0
# v
list.insert(0, 1)
# vi
for i in range(len(list)):
    list[i] = list[i] + 10

# vii
for i in range(len(list)):
    list[i] = 10

# viii
for i in range(len(list)):
    list[i] = list[i] + i

# ix
del list
print(list) 

# Qn 43
def square_no():
    list = []
    num = int(input("How many square numbers to generate? "))
    for x in range(0, num):
        squared = x ** 2
        list.append(squared)
    print(list)
        
square_no()

# Qn 44
def fibo_no():
    list = []
    a, b = 0, 1
    num = int(input("How many Fibonacci numbers to generate? "))
    
    for _ in range(num):   # loop body executed num times
        list.append(a)
        a, b  = b, a + b
        
        
    print(list)

fibo_no()

# Qn 45
def function():
    list = []
    while True:
        input1 = input("Enter an ineger (enter QUIT to quit): ")

        if input1 == "QUIT":
            break
        else:
            list.append(int(input1))
        list1 = ", ".join(map(str, list)) 

    print("You have entered: " + list1, end=".")

function()

# Qn 46
def function():

    list_element = []
    list_index = []
    index_no = 0

    len_list = int(input("How many numbers are in the list? "))

    for x in range(len_list):
        element = input("Enter list element: ")
        index_no = x
        list_element.append(element)
        list_index.append(index_no)
    
    reversed = list_element[::-1]
    index_name = ['Index']
    list_name = ["List"]
    reverse_name = ["Reverse"]

    print("You have entered: ")
    for rn, ln, i_n in zip(index_name, list_name, reverse_name):
        print("{:<5} {:<5} {:<7}".format(rn, ln, i_n))
    
    for index1,element1, reversed1 in zip(list_index, list_element, reversed):
        print("{:<5} {:<5} {:<7}".format(index1, element1, reversed1))

function()

# Qn 47
def function():
    dict1 = {
        "first_name": "Amanda", 
        "last_name": "Smith",
        "age": 20
    }

    print(dict1["first_name"])

    dict1["last_name"] = "Harrison"

    print(dict1["last_name"])

    dict1["user_email"] = "a.harrison@gmail.com"

    print(dict1)

    dict1.pop("age")
    print(dict1)

    
function()

# Qn 48

def function1():
    state_abb = {
        "NSW": "New South Wales",
        "ACT": "Australian Capital Territory",
        "NT": "Northern Territory",
        "QLD": "Queensland",
        "SA": "South Australia",
        "TAS": "Tasmania",
        "VIC": "Victoria",
        "WA": "Western Australia"
    }
    variable_to_extract = [3, 6]
    variable = [list((state_abb.keys()))[index] for index in variable_to_extract]
    print(variable)
function1()

# Qn 49

def function1():
    state_abb = {
        "NSW": "New South Wales",
        "ACT": "Australian Capital Territory",
        "NT": "Northern Territory",
        "QLD": "Queensland",
        "SA": "South Australia",
        "TAS": "Tasmania",
        "VIC": "Victoria",
        "WA": "Western Australia"
    }
    state = input("Enter state NSW/ACT/NT/QLD/SA/TAS/VIC/WA: ")
    state_upper = state.upper() 
    x = state_abb[state_upper]
    print(f"You have entered {x}")
function1()

# Qn 50
def function():

    dict1 = {}

    key = input("Enter a key (string): ")
    value = input("Enter value: ")
    dict1[key] = value
    key = input("Enter a key (string): ")
    value = input("Enter value: ")
    dict1[key] = value
    
    print("We have a dictionary: " + str(dict1))


function()

# Qn 51
def func():
    dic1 = {12:144, 13:169}
    dic2 = {3:33, 4:44}
    dic3 = {5:510,6:632}
    dic4 = {**dic1, **dic2, **dic3}
    print(dic4)
func()

# Qn 52
school = {
    "classA": {
        "student": {
            "name":"Merlion Tan",
            "subjects":{                  
                    "phython":70,
                    "communications":80   
          } } }}
print(school["classA"]['student']["subjects"]["communications"])

# Qn 53

""" failed
list = []
sampleDict = {
    "name": "Kelly",
    "interest": "badminton",
    "age": 32,
    "town": "Ang Mo Kio" }
for x in sampleDict.keys():
    list.append(x)
if len(list) > 3: # idk why need this but ok. check if got enough numbers to prevent error???
    list[3] = "district"

sampleDict = list



print(sampleDict)
"""
sampleDict = {
    "name": "Kelly",
    "interest": "badminton",
    "age": 32,
    "town": "Ang Mo Kio" }

sampleDict["district"] = sampleDict.pop("town")  # sampleDict.pop("town") = "Ang Mo Kio"

print(sampleDict)


# Qn 54

inventory = {
    'coins' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'haversack' : ['wooden spear', 'dagger', 'fish', 'drumstick']
}

inventory["equipped"] = ["ruby", "red potion", "apple"]
inventory["haversack"].sort()
inventory["haversack"].remove("dagger")
inventory["coins"] = 500 + 50
print(inventory)

# Qn 55
def func():
    stock = {
        "sunblock": 25,
        "swimming cap": 2,
        "ear plugs": 4,
        "goggles": 15
        }
    unit_price = {
        "sunblock": 16,
        "swimming cap": 10,
        "ear plugs": 1.5,
        "goggles": 9.9
        }
    avail_stock = stock.keys()
    print(avail_stock)
    
    price_sunblock =stock["sunblock"] * unit_price["sunblock"]
    price_swim = stock["swimming cap"] * unit_price["swimming cap"]
    price_ear = stock["ear plugs"] * unit_price["ear plugs"]
    price_gogg = stock["goggles"] * unit_price["goggles"] 

    total_price = (price_ear + price_gogg + price_sunblock + price_swim) * 1.07
    dp2 = "{:.2f}".format(total_price)


    print("Checkout price: $" + dp2)                                          
    

func()

# Qn 56

def triple(sentence):
    list = []
    for letter in sentence:
        x = letter*3
        list.append(x)
        y = "".join(list)
    
    print(y)
    
triple('Uni')
# output : UUUnnniii

def triple(sentence):
    trip = "".join([letters*3 for letters in sentence])
    print(trip)
triple("Uni")
# output : UUUnnniii

# Qn 57

def triple():
    sentence = input("Enter a sentence: ")
    trip = "".join([letters*3 for letters in sentence])
    print("Triple effect: " + trip)


triple()

# Qn 58
def filter_digit(i):

    list = []
    intlist = []

    for char in i:
        
        if char.isdigit():
            list.append(char)
            intlist.append(int(char))

    
    value1 = "".join(list)
    print(value1)
    totalsum = sum(intlist)
    print(totalsum)


filter_digit("0a1bb5cdef77")

# output: 01577 and 20

# simplify code

def filter_digit(i):
    value = "".join(char for char in i if char.isdigit())
    sumvalue = sum(int(char) for char in value)

    print(value)
    print(sumvalue)

filter_digit("0a1bb5cdef77")

# Qn 59

def is_prime_number(arg1):
    if arg1 < 1:
        print(False)
        return
    
    for divisor in range(2, arg1 - 1):
        if arg1 % divisor == 0:
            print(False)
            return
    else:    
        print(True)

        
is_prime_number(97)

# Qn 60
def get_next_prime_number(int1):
    
    for divisor in range(2, int1 - 1):
        if x % divisor == 0:
            continue
        else:
            print(x)
            break
                
                 
get_next_prime_number(3)
          

def is_prime_number(x):
    
    if x < 2:
        return False
    for divisor in range(2, int(x**0.5) + 1):
        if x % divisor == 0:
            return False
    return True

def get_next_prime_number(int1):
    
    next_number = int1 + 1
    while True:
        if is_prime_number(next_number) == True:
            print(next_number)
            return next_number
        else:
            next_number += 1

result = get_next_prime_number(29399)
print(result)

# Qn 61
def bin_to_dec(str1):
    blist = []
    list1 = []
    for number in str1:
        blist.append(number)
    blist.reverse()

    y = -1
    for value in blist:          # [0, 1, 0, 1]
        y += 1
        x = int(value) * 2 ** y
        list1.append(x)

    return_value = sum(list1)
    print(return_value)


bin_to_dec("10101001110100011")

# Qn 62 - Qn 64

class Employee:
    def __init__(self, first_name, last_name, number, position, phone_ext):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.position = position
        self.phone_ext = phone_ext
# Qn 64
    def __str__(self):
        return f"Employee({self.number}, {self.first_name}, {self.last_name}, {self.position}, {self.phone_ext})"

# Qn 66
    def __repr__(self):
        return f"Employee({self.number}, {self.first_name}, {self.last_name}, {self.position}, {self.phone_ext})"

    def print_details(self):
        print(f"----------------E {self.number}--")

        fullname = list([f'{self.first_name} {self.last_name}'])
        line = ["|"]
        position = [f'{self.position}']
        ext = [f"{self.phone_ext}"]
        
        for line1, fullname1, line1 in zip(line, fullname, line):
            print("{:<2}{:<24}{:>1}".format(line1, fullname1, line1))
        for line1, position1, line1 in zip(line, position, line):
            print("{:<2}{:<24}{:>1}".format(line1, position1, line1))
        for line1, ext1, line1 in zip(line, ext, line):
            print("{:<2}{:<24}{:>1}".format(line1, ext1, line1))
        
        print("---------------------------")


p1 = Employee("John", "Smith", 1234567, "Software Engineer", "ext 4567")
rep = repr(p1)
john = Employee("John", "Smith", 1234567, "Software Engineer", "x4567")

print(p1)  # Qn 65
print(rep)
john.print_details()

# Qn 70
class Course:
    def __init__(attri, description, course_code, credits):
        attri.description = description
        attri.course_code = course_code
        attri.credits = credits
    
class Department:
    def __init__(attri1, name, department_code, courses):
        attri1.name = name
        attri1.department_code = department_code
        attri1.courses = {
                "courses" :""
            }
    def add_course(attri1):
        print("this is a placeholder")

class Student:
    def __init__(attri2, name, student_number, modules):
        attri2.name = name
        attri2.student_number = student_number
        attri2.modules = modules

csit_dept = Department("Computer Science and Information Technology", "CSIT")
csit110 = csit_dept.add_course("Fundamental Programming with Python", "CSIT110", 6)
gunther = Student("Gunther", "Tan")
gunther.enrol(csit110)

print(csit_dept)





# Qn 76
class Pizza:
    def __init__(attri, ingredients):
        attri.ingredients = ingredients

    def __repr__(attri):
        return (f"{attri.ingredients}")

# Qn 77
class Margherita(Pizza):
    def __repr__():
        return
        

ingredients = Pizza(["mozzarella", "tomatoes"])

print(f"ingredients:{ingredients}")

class MyClass:
    def __init__(self, name, values):
        self.name = name
        self.values = values

# Creating an object of MyClass with a list as a constructor argument
my_object = MyClass("Example", [1, 2, 3, 4, 5])

# Accessing the attributes of the created object
print(f"Object Name: {my_object.name}")
print(f"Object Values: {my_object.values}")




def get_assessment_mark():
    mark_list = []
    while True:
        try:
            a_mark = int(input("Enter assignment mark (0-20): "))
            if a_mark in range(0, 21):
                mark_list.append(a_mark)
                
            elif a_mark not in range(0, 21):
                print("Error: assignment mark must be between 0 and 20")
                break
                                    
        except Exception:
            print("Error: assignment mark is invalid")
            break
        
        try:
            p_mark = int(input("Enter project mark (0-30): "))
            if p_mark in range(0, 31):
                mark_list.append(p_mark)
                
            elif p_mark not in range(0, 31):
                print("Error: project mark must be between 0 and 30")
                break

        except Exception:
            print("Error: project mark is invalid")
            break

        try:
            fe_mark = int(input("Enter final exam mark (0-50): "))

            if fe_mark in range(0, 51):
                mark_list.append(fe_mark)
                
            elif fe_mark not in range(0, 51):
                print("Error: final exam mark must be between 0 and 50")
                break

        except Exception:
            print("Error: final exam mark is invalid")
            break

        mark_sum = sum(mark_list)
        print("Total mark: ", mark_sum)
        break

get_assessment_mark()

# Qn 80
class Student:

    def __init__(attri2, name, student_number):
        attri2.name = name
        attri2.student_number = str(student_number)
        attri2.modules = []
        
    def add_module(attri2, module):
        attri2.modules.append(module)


    def from_list(attri2, student_list):
        all_student = []
        for _ in student_list:
            student1 = [attri2.name, attri2.student_number]
            all_student.append(student1)
    
        student_list = []
        while True:
            john = Student("John Snow", 135226)
            peter = Student("Peter Parker", 197439)
            student_list.append(john, peter)
    from_list()



class Student:
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = str(student_number)
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    @classmethod
    def from_list(cls, student_list):
        all_students = []
        for student_data in student_list:
            student = cls(student_data[0], student_data[1])
            all_students.append(student)
        return all_students

if __name__ == "__main__":

    student_data_list = []

    student_data_list.append(("John Snow", 135226))
    student_data_list.append(("Peter Parker", 197439))
    

    students = Student.from_list(student_data_list)

    # Adding modules to students
    students[0].add_module("cs")
    students[1].add_module("math")

    for student in students:
        print(f"Name: {student.name}, Student Number: {student.student_number}, Modules: {student.modules}")

    print(student_data_list) 
    print(students)







#assignment2 qn 3
def get_car_rental_booking():
    eco_car = int(input("Number of Economy cars: "))
    stand_car = int(input("Number of Standard cars: "))
    prem_car = int(input("Number of Premium cars: "))
    suv_car = int(input("Number of SUVs: "))
    rent_duration = int(input("Rental duration (number of days): "))
    rent_duration1 = int(rent_duration)
    subtotal = int(eco_car) + int(stand_car) + int(prem_car) + int(suv_car)

    eco_car_price = int(eco_car * 40 * rent_duration1)       # find out price of rental
    stand_car_price = int(stand_car * 70 * rent_duration1)
    prem_car_price = int(prem_car * 100 * rent_duration1)
    suv_car_price = int(suv_car * 130 * rent_duration1)
    subtotal_price = int(eco_car_price + stand_car_price + prem_car_price + suv_car_price)
    price_w_tax = int(subtotal_price * 1.18)

    ec_price_2dp = "${:.2f}".format(eco_car_price)            # format to 2dp
    sc_price_2dp = "${:.2f}".format(stand_car_price)
    pc_price_2dp = "${:.2f}".format(prem_car_price)
    suvc_price_2dp = "${:.2f}".format(suv_car_price)
    subtotal_price2dp = "${:.2f}".format(subtotal_price)
    price_w_tax2dp = "${:.2f}".format(price_w_tax)

    names = ["Economy", "Standard", "Premium", "SUV", "Subtotal"]
    no_of_cars = [eco_car, stand_car, prem_car, suv_car, subtotal]
    price = [ec_price_2dp, sc_price_2dp, pc_price_2dp, suvc_price_2dp,subtotal_price2dp]

    name1 = ["Total (18% tax)"]
    price1 = [price_w_tax2dp]

    print()
    print(f"Summary of your car rental for {rent_duration1} day(s)")

    for name, no_of_car, car_price in zip(names, no_of_cars, price):
        print("{:<13} {:^3} {:>10}".format(name, no_of_car, car_price))
    for name2, price2 in zip(name1, price1):
        print("{:<16}  {:>10}".format(name2, price2))

get_car_rental_booking()

# qn 2
def get_cpf_interest_rates():
    age = int(input("Enter current age: "))

    OA = input("Enter current amount in OA: ")
    OA1 = int(OA)
    OA_rate = OA1 * 0.025

    SA = input("Enter current amount in SA: ")
    SA_rate = int(SA) *0.04

    MA = input("Enter current amount in MA: ")
    MA_rate = int(MA) * 0.04

    if age < 55:
        RA_rate = 0
        if OA1 > 20000:
            OA1 = 20000
        extra = int((OA1 + int(SA) + int(MA)))
        if extra > 60000:
            extra_i = 60000 * 0.01
        else:
            extra_i = extra * 0.01
    else:   # if age is > 55
        RA = input("Enter current amount in RA: ")
        RA1 = int(RA)
        RA_rate = int(RA1) * 0.04
        if OA1 > 20000:
            OA1 = 20000
        extra = int(OA1 + int(SA) + int(MA) + RA1)
        extra1 = int(extra)
        if extra1 > 30000:
            extra_i = (30000 * 0.02) + ((extra1 - 30000) * 0.01)
        else:
            extra_i = extra * 0.02
    

    total_rate = OA_rate + SA_rate + MA_rate + RA_rate + extra_i
    total_rate_2dp = "{:.2f}".format(total_rate)  # format to 2dp

    print("Your interest rate this year will be $" + str(total_rate_2dp))


get_cpf_interest_rates()

# qn 4
def sanitize_vehicle_filenames():

    cleansed_list = []

    while True:  # while True creates an infinite loop
        filename = input("Filename?")

        if not filename:  # detects if user enters an empty string
            break

        cleansed_file = ""
        bracket_count = 0

        for virus in filename:
            if virus == '<':
                bracket_count += 1
            elif virus == '>':
                bracket_count -= 1
            elif bracket_count == 0:
                cleansed_file += virus

        cleansed_list.append(cleansed_file)

    return ",".join(cleansed_list)


x = sanitize_vehicle_filenames()                 # Call the function
print(x)