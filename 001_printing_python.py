name = "Timothy Unkert"
age = 46

# constant variable - this is a convention, you can change it ... but DON'T!
PI = 3.1415

other_name = "Joe Smith"
other_age = 49  # notice these variables are in snake case

print(name)
print(age)

print("My name is " + name + ".")  # concatenating a string variable to other strings

# print("My age is " + age + " years old.")  # this will throw an error because age is the wrong type

print("My age is " + str(age) + " years old.")  # this will work because of 'type conversion'
