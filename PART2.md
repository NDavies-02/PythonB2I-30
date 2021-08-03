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

**New dictionary**: dict = {"Mon":1, "Tue":4, "Wed":3}

**Delete item**

del dict["Tue"]

New dictionary: dict = {"Mon":1, "Wed":3}



- Each key should be unique
