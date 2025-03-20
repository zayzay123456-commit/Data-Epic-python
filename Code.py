# 1. Identification and printing different types of values using type()
a = "Zainab"
b = 50
c= 10.5
d= True
e = [1,2,3,4]
f =(4,5,"Mango")
g = {1,2,3,4,5}
h={"Name": "Alice", "Age" :"25"}

print(type(a)) 
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

# Performing basic arithmetic using integer and Float
add_result= b+c
Multiply_result =b*c
Subtract_result =b-c
Divide_result = b/c

print("addition",add_result)
print("Multiplication",Multiply_result)
print("Subtract",Subtract_result)
print("Divide",Divide_result)

# Convert between different Numerical type using integer and float
print("Float to integer" , c)
print("integer to Float" , b)

# Using String method to Manipulate text
text ="Zainab is a good girl"
upper_text =text.upper()
print("uppercase:",upper_text)
lower_text =text.lower()
print("lowercase:",lower_text)
capitalized_text=text.capitalize()
print("capitalized:", capitalized_text)
title_text =text.title()
print("titled_case",title_text)
new_text = text.replace("good","Bad")
print("Replaced:", new_text)
new_text=text.replace("Zainab","Madina")
print("Replaced",new_text)
position= text.find ("Zainab")
print("position of'Zainab':",position)

# Formatting Strings in different way
Name = "Zainab"
Course ="Medicine"
formatted_string = f"My name is {Name} and i am studying {Course}"
print(formatted_string)
formatted_string = "My name is {0} and i am studying {1}". format (Name,Course)
print (formatted_string)

# Creating a list, acess elements using indexing and Slicing
states = ["Oyo","Ogun","Niger","Rivers", "Ondo","Ekiti"]
# Acessing Elements using Index
print(states[0])
print(states[3])
print(states[5])
print(states[-1])

# Acessing Elements Using Slicing
print(states[1:4])
print(states[:2])
print(states[-1:])

# Performing list Operations
# Appending states
states.append ("Nassarawa")
print(states)
# Removing States
states.remove("Ekiti")
print(states)
# Sorting states
states.sort()
print(states)
# Reversing states
states.reverse()
print(states)

# Creating a tuple, acessing elements and demonstrate tuple immutability
fruits =("mango","Pawpaw","Cashew","Orange","Apple","Pineapple")
print(fruits)
# Accessing Element
print(fruits[1])
print(fruits[2:4])
fruits.remove("mango")
print(fruits)
