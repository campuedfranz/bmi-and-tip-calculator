#Data Types

#String
print("Hello"[0]) #subscripting

#Integers
integer_name = 123

#Float
float_name = 3.141516

#Boolean
boolean_name = True

#type() function: determines the data type
print(type(boolean_name))

#Type conversion
print(type(str(123)))
print(type(int("5")))
print(type(float(10)))

#Math operators + - * / **(exponent)
#Heirarchy () ** * / + -
#(/ *) is in same rank so you need to prioritize the operation in left
#(+ -) is in same rank so you need to prioritize the operation in left
# += -= *= /= e.g score+=1 is the same as score = score + 1 (useful in updating previous values)

#Number Manipulation
#round()
#converting float into int just chop off decimal numbers
# / single  means division and returns float data type
# // double means division but returns int and decimals got chopped off

#f-strings
#No need to convert other data types to string to concatenate them to a string
my_age = 26
print("My age is " + str(my_age))
print(f"My age is {my_age}")