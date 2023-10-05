# """ 
# In Python, an escape character is used to represent characters that are difficult or impossible to type directly in a string. Escape characters are preceded by a backslash `\` and are used to include special characters within a string. Here are some common escape characters in Python:

# 1. `\n`: Represents a newline character. It is used to start a new line within a string.

# python
# print("Hello\nWorld")


# Output:

# Hello
# World

# """
# """
# 2. `\t`: Represents a tab character. It is used to insert a tab within a string.

# python
# print("Hello\tWorld")


# Output:

# Hello   World

# """
# """
# 3. `\\`: Represents a literal backslash character. It is used when you want to include a backslash in a string.

# python
# print("This is a backslash: \\")


# Output:

# This is a backslash: \

# """
# """
# 4. `\'` and `\"`: Represents single and double quotation marks, respectively, within a string.

# python
# print("She said, \"Hello!\"")
# print('He\'s a programmer.')


# Output:

# She said, "Hello!"
# He's a programmer.

# """
# """
# 5. `\r`: Represents a carriage return character. It is used to move the cursor to the beginning of the current line, effectively overwriting the text on that line.

# python
# print("Overwrite this line.\rNew text.")


# Output:

# New text.line.

# """
# """
# 6. `\b`: Represents a backspace character. It is used to move the cursor one position backward.

# python
# print("Hello\bWorld")


# Output:

# HellWorld

# """
# """
# 7. `\uXXXX` and `\UXXXXXXXX`: Represents Unicode characters using their hexadecimal values. `\u` is used for 16-bit Unicode characters, and `\U` is used for 32-bit Unicode characters.

# python
# print("This is a smiley face: \U0001F604")


# Output:

# This is a smiley face: 😄
# """