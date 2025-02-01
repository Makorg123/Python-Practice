# ## Type inferencing
age = 33
print(type(age))
name = "Anas"
print(type(name))
if True:
    print("Correct Indentaion")
    if False:
        print("This one print")
    print("This will print")
print('Outside the if block')
# converting type conversion
age = 24

age_str = str(age)
print(type(age))
print(type(age_str))

age_float = float(age)
print(type(age_float))


# Dynamic typing: python allows the type of a variable to change as the program executes

var = 10
print(var, type(var))

var = 'Hello'
print(var, type(var))

var = 3.14
print(var, type(var))
age = int(input('What is your age: '))
print(age, type(age))