""" A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

Creating a Function
In Python a function is defined using the def keyword: """


def my_function():                  #function creating using 'def' keyword
  print("Hello from a function")

my_function()                       #function call

""" Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly: """
def greet_person(greeting, *names):
    for name in names:
        print(greeting, name)

greet_person("Hello", "Alice", "Bob", "Charlie")

""" Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

Example: """

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

"""
The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

Example """
def myfunction():
  pass