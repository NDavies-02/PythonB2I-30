# Notes
The following are my notes for key concepts from the lectures.

## Lists ##
`list[start:end]` - Get multiple items between and inclusive of the specified indices.

If start=1 and end=3, we would get the 2nd, 3rd, 4th item in the list.

`del list[index]` - delete item in list

## Arithmetic Operations & Strings ##
The only operators that work on strings are:
1. **Addition** - acts as concatenation [+]
2. **Multiplication** - Repeat the string y times. Example: `'h'*3='hhh'`

## Multiple Assignment ##
Assign multiple variables at once: `var1, var2, var3 = val1, val2, val3` respectively

## Dictionaries ##
Uses **value pairs**:
`dict = {"Mon":1, "Tue":2, "Wed":3}`

The key in this case would be the value before the colon.
So `print(dict["Mon"])` would get you `1`.

**Updating dictionaries**

*Example: Update "Tue" to 4* - `dict["Tue"] = 4`

**New dictionary**: `dict = {"Mon":1, "Tue":4, "Wed":3}`

**Delete item**

`del dict["Tue"]`

**New dictionary**: `dict = {"Mon":1, "Wed":3}`
*Note*: Each key should be unique

## Tuples ##
**Recap of lists and dicts**

`list = ["item1", "item2"]`

`dict = {"key1":value1, "key2":value2}`

**Creating a tuple**

`tup = ('item1', 'item2', 'item3')`

**The most important thing about a tuple**: They cannot be updated. It is more like a read-only list - so you can access all the functions of lists such as slicing but you just can't change the values.

In regards to deletion, you must delete the whole tuple, you cannot remove a single value.
(Note you can still refer to a single value using indexes as you would in a list).

You can combine tuples together, but the result must be in a new tuple.

**Won't work**: `tup1 = tup1 + tup2` - as this would be trying to edit tup1

**Instead, do**: `tup3 = tup1 + tup2` - as this makes a new tuple

## Conditional Statements ##
```
if condition:
    do something
elif some other condition happens:
    do something else
else:
    If no previous conditions met, do this
```
This is useful for executing code based on input, comparing values and much more.
## Iteration ##
### For Loops ###
```
for item in list:
    Do stuff.
```
This 'stuff' which is your code, will be run over and over again for each item in list. A basic example would be to print each item in the list - `print(item)`.

You can also specify ranges of numbers - `for i in range(start, end)`
And you can write loops within loops. known as **nested loops**.
### While Loops ###
Code within a while loop is executed whilst the specified condition is true.
It will stop only when the condition is no longer true. If the condition is forever true, an **infinite loop** is caused.

**Syntax**
```
while condition:
    do this code
```
    
**Example**
```
x=100
while x>=50:
    print(x)
    x=x-1
```
This would print numbers in descending order, 100 to 50. As once it gets to 49 the condition is no longer met, so the code within the loop stops.
#### Key Loop Functions ####
`break`: When this line is reached, stop executing the code in the loop.

`continue`: Carry on looping (skip anything after the continue statement).

`pass`: Acts as filler code but does not do anything. A good placeholder.

## Try and Except ##
Useful for cases where there is a good possibility the code will break. For example, code that relies on user input. It prevents the code from crashing completely.
Python will try to run the code. If there is an *exception* (i.e. something goes wrong), using the except statement provides a fall-back (for example, print an error) that will be run instead of the program crashing.

It is a good idea to keep the except code simple so that it doesn't crash itself...

**Syntax**
```
try:
    to run this code
except:
    if something goes wrong there, do this instead.
```    
## Functions ##
Functions can be used to wrap related lines of code that perform a particular job together.
When you add items to a list for example, you are using built-in functions. (Multiple related functions are often put in classes).

**Defining a function**
```
def funcName(params):
    print("any code can go in a function")
    valToReturn=13
return valToReturn
```

When you call a function, you can store a returned value in a global variable:

`var1=funcName`

In this case, `var1` would contain 13.

## Object Oriented Programming (OOP) ##
In object-oriented programming, a key idea is **classes**.
And **objects** are instances of classes, of which you can have multiple.

**To define a class in Python**:

```class className:
    def funcName(self, anyOtherParams):
        code
```
When you create a function within a class, the function must have the parameter self, regardless of it using any other parameters.

**To call a function within a class**:

First you must create an object.
`objName = className`

Then you can call any function from the object.
`objName.funcName(anyOtherParams)`

## Inheritance ##
Imagine you created a class called `parentClass`.
You want to make another class that inherits properties and functionality of `parentClass`, say, `childClass`.

That is essentially the point of inheritance.
When you create a child class from a parent class, the child will inherit all of the functions of the parent class, **as well as** having its own functions.

**Example**

**Create parent class**

```
class Parent
    def parentFunc(self):
        parentFuncCode goes here
```

**Create child class**
```
class Child(Parent)

    def childFunc(self):

        childFuncCode goes here
```

**Call parentFunc from parent class**

```
p = Parent
p.parentFunc()
```
*This would execute the code in parentFunc*

**Call childFunc from child class**
```
c = Child
c.childFunc() - this would execute the code in childFunc
```

**Call parentFunc from child class**

`c.parentFunc()` - this would execute the code in `parentFunc` inherited from the parent class but still from the child.

*Example use case*

You could have a parent class for People, and child classes for Male and Female.

### Redefining functions ###
You can redefine a parent's function within a child simply by creating a function within the child of the same name.

## End of notes ##
