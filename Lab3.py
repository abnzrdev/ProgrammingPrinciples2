# A basic function
def my_function():
    print("Hello from a function")

# Function called after being defined (note: previous definition is overwritten)
def my_function():
    print("Hello from a function")
my_function()

# Function with one argument
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Function with two arguments
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Refsnes")

# Function call with missing argument (this will raise an error)
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil")

# Function with arbitrary number of arguments (*args)
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

# Function with named arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Function with arbitrary keyword arguments (**kwargs)
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

# Function with default parameter value
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Function that accepts a list
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Function with return statement
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# Empty function with pass
def myfunction():
    pass

# Function with positional-only argument
def my_function(x, /):
    print(x)
my_function(3)

# Function with keyword argument
def my_function(x):
    print(x)
my_function(x = 3)

# Function with positional-only argument (will raise error with keyword)
def my_function(x, /):
    print(x)
my_function(x = 3)

# Function with keyword-only argument
def my_function(*, x):
    print(x)
my_function(x = 3)

# Normal function call
def my_function(x):
    print(x)
my_function(3)

# Keyword-only argument (will raise error if passed positionally)
def my_function(*, x):
    print(x)
my_function(3)

# Combination of positional-only and keyword-only arguments
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)

# Recursive function
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("Recursion Example Results:")
tri_recursion(6)

# Simple lambda with one argument
x = lambda a : a + 10
print(x(5))

# Lambda with two arguments
x = lambda a, b : a * b
print(x(5, 6))

# Lambda with three arguments
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Lambda returning function (closure)
def myfunc(n):
    return lambda a : a * n

# Using a lambda doubler
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

# Using a lambda tripler
def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))

# Using both doubler and tripler
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
