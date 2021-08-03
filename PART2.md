# PART 2 Notes
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
Important: Each key should be unique

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
`if condition:
    do something
elif some other condition happens:
    do something else
else:
    If no previous conditions met, do this`
This is useful for executing code based on input, comparing values and much more.
## Iteration ##
### For Loops ###
`for item in list:
    Do stuff.`
This 'stuff' which is your code, will be run over and over again for each item in list. A basic example would be to print each item in the list - `print(item)`.

You can also specify ranges of numbers - `for i in range(start, end)`
And you can write loops within loops. known as **nested loops**.
