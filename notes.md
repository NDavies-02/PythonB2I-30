# Notes
The following are my notes for key concepts from the lectures.

## Section 1: Intro ##
Use a `%` sign for MOD

Use double asterisk for exponents, e.g. 2^3 is 2**3 in Python

## Section 2: Modules and Functions ##
`import  module` - Imports the specified module so you can use its functions in your code.

`module.function(param)` - Call a function from a specific imported module and specify its parameters.

`function(parameters)`

## Section 3/4: Strings/Slicing/Lists ##
`list = [1,2,3,4,5,6]` - Define a list with the \[elements]

Slice this list to **show only the numbers 3-5**:

`list[2:4]`

`'something' in variable` - search for something (string) in var (of type string)

`list("string")` - Take each char of string and put into a list

`len(list)` - How many elements in list?

`max(list)` - What's the largest value of the list?

`min(list)` - What's the smallest value of the list?

## Section 7: Functions ##
`def functionname (*parameter)` - Allows multiple entries for a single parameter - forms a list.

When defining a function, a specific value can be used as so: `function(param[index])`.

## Section 8: OOP ##
`class ClassName:`

    `def funcName(self, params):`

        `functioncode`

Note the '`self`' parameter.

- Classes act as wrappers for multiple related functions.

- Call a function: `ClassName.funcName()` (like how you call functions from libraries)

- You can assign classes to variables.

Example: You have the following class

`class Class1 (params):`

    `var="text"`

You can access `var` using:

`var2=Class1(params)`

`print(var2.var)`
Result: "text"

## File Handling ##
**File Operations**
**Note** that each file you open should be assigned to a variable. So you can open multiple files. Each variable that is a file type will have the following functions applicable to them.
- Open a file in read/write mode - `var=open("Path_to_file", "r/w")`

- Write to open file - `var.write(textToWrite)`

- Close File - `var.close()`

- Read from a file - first open file, then `var.read(charsToRead)`

Using `file.read()` reads the whole file. However, it tracks what part of the file has been read. So if you were to subsequently use `file.readline()` nothing would appear as there is no more content to read.

**So what if we want to go back to an earlier point in the file?**

`file.seek(0)` - move cursor to start of file

**Recap: Reading Files**

`file.readline(lineNo)` - reads a single line from the file.

`file.readlines()` - reads multiple lines from the file as a list.

**Editing via reading**

You could use this property of `readlines()` to edit the file. Read the lines into a list assigned to a variable. Then you can freely edit the list, and write the new list into the file.

`file.writelines(listtowrite)` - Write the list into the file. Note you should use `/n` for newlines within the file.
## End of notes ##
