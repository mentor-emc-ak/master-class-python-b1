# Creating a List
a = [1, 2, 3, 'Python', 3]

# Accessing elements by indexing
print(a[0]) 
print(a[-1]) 

# Modifying an element
a[1] = 'Updated'
print(a)  

# Appending an element
a.append(4)

# Removing an element
a.remove(3)

# List slicing
print(a[1:3])


# Creating a Set
s = {1, 2, 3, 'Python', 3}
print(s) 

# Adding elements
s.add(4)

# Removing elements
s.remove(3)  # KeyError if the element is not present

# Accessing elements (No indexing because it is unordered)
for element in s:
    print(element)

set_converted = list(s)
print("this is set value", set_converted[0])



# Creating a Tuple
tup = (1, 2, 3, 'Python', 3)

# Accessing elements by indexing
print(tup[0])
print(tup[-1])

# Tuple slicing
print(tup[1:4])

# Attempting to modify a tuple (Raises TypeError)
# tup[1] = 'Updated'  # Uncommenting this will raise an error



# Arithmetic Operations

a = 1
b = 2

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus

# Comparison Operators

print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to

# Logical Operators

print(a > 0 and b > 0)  # Logical AND true and true = true | false and true = false | true and false = false | false and false = false
print(a > 0 or b < 0)   # Logical OR true or true = true | false or true = true | true or false = true | false or false = false
print(not (a > 0))      # Logical NOT true = false | false = true

print((a > 0 and b < 0) or (a < 0 or (a == 0)))  # Logical AND and OR combined
#      true             or (false or false)


number = -2

# 15 % 2 = 1
# 14 % 2 = 0

if number == 0:
    print("This Neither Even Nor Odd")
elif number < 0:
    print("Negative")
elif (number % 2) == 0:
    print("Even")
else:
    print("Odd")



# Using the 'in' operator to check for membership

