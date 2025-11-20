print("Welcome to the Python program!")
print("Shee Ganeshay Namah:")

name = "Nitin"
print("My name is", name)
print(type(name))
age = 32
print("My age is", age)
print(type(age))

learning = True
print("I am learning Python:", learning)
print(type(learning))

# Calculate monthly balance
"""
income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))
print("Balance:", income - expenses)
"""
print('Hello, \n"How are you?\\newline')

print("Hello", "Nitin")
print("Hello", "Nitin", sep=" - ", end="!\n")

# If-elif-else statement
age = 32
if age > 18:
    print("You are an adult.")
elif age == 18:
    print("Ready for license.")
else:
    print("You are a minor.")

# Match-case statement
status = 200
match status:
    case 200:
        print("HTTP.OK")
    case 404:
        print("HTTP. Not Found")
    case 500:
        print("HTTP. Internal Server Error")
    case _:
        print("HTTP. Unknown Status")

# For loop
for i in range(5):
    print("Iteration:", i)

# While loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

for i in range(1, 11):  # Complete the range
    print("56 x ", i, "=", (56 * i))  # Complete the calculation

# Different ways to define strings
name = "nitin"
name = "nitin"
name = """nitin"""
name = """nitin"""
name = """nitin
is
python
expert
"""
# String Indexing
name = "nitin"
print(name[0])  # Output: n
print(name[1])  # Output: i
print(name[2])  # Output: t
print(name[3])  # Output: i
print(name[4])  # Output: n

print(name[-1])  # Output: n
print(name[-2])  # Output: i
print(name[-3])  # Output: t
print(name[-4])  # Output: i
print(name[-5])  # Output: n

# String slicing
expertise = "Python"
print(expertise[0:2])  # Output: 0 to 2-1, ie 0 to 1

description = "I am learning Python programming"
print(description[5:13])  # Output: 5 to 13-1, ie 5 to 12
print(description[0:10:1])  # Output: 0 to 10-1 with step 1
print(description[0:10:2])  # Output: 0 to 10-1 with step 2
print(description[:10])  # Output: start to 10-1
print(description[10:])  # Output: 10 to end
print(description[:])  # Output: start to end

# String Methods
message = "  Hello, Nitin! Welcome to Python programming.  "
print(message.lower())  # Convert to lowercase
print(message.upper())  # Convert to uppercase
print(message.strip())  # Remove leading and trailing whitespace
print(message.replace("Nitin", "User"))  # Replace substring
print(message.split(" "))  # Split string into a list
print(message.find("Python"))  # Find substring index
print(message.count("o"))  # Count occurrences of substring
print(message.startswith("  Hello"))  # Check if string starts with substring
print(message.endswith("programming.  "))  # Check if string ends with substring
print(message.capitalize())  # Capitalize first character
print(message.title())  # Title case
print(message.center(50, "-"))  # Center string with padding
print(message.isalpha())  # Check if all characters are alphabetic
print(message.isdigit())  # Check if all characters are digits
print(message.isspace())  # Check if all characters are whitespace
print(len(message))  # Get length of string
print(message.index("Nitin"))  # Get index of substring
print(message.count(" "))  # Count spaces in the string
print(message.swapcase())  # Swap case of characters
print(message.partition("Nitin"))  # Partition string at substring
print(message.rfind("o"))  # Find last occurrence of substring
print(message.zfill(60))  # Pad string on the left with zeros to a total width of 60
print(message.encode())  # Encode string to bytes
print(message.expandtabs(4))  # Expand tabs to spaces with a tab size of 4
print(message.format(name="Nitin"))  # Format string with named arguments
print(message.format_map({"name": "Nitin"}))  # Format string with a mapping
print(message.translate(str.maketrans("Nitin", "User")))  # Translate characters
print(message.removeprefix("  Hello,"))  # Remove prefix from string
print(message.removesuffix("programming.  "))  # Remove suffix from string
print(message.islower())  # Check if all characters are lowercase
print(message.isupper())  # Check if all characters are uppercase
print(message.isprintable())  # Check if all characters are printable

# F-Strings
name = "Nitin"
age = 32
print(f"My name is {name} and I am {age} years old.")
print(f"In five years, I will be {age + 5} years old.")
print(f"{name.upper()} is learning Python.")
print(f"{name} has {len(name)} characters in his name.")
print(f"{name:^20} is centered in a field of width 20.")
print(f"{name.lower():<20} is left-aligned in a field of width 20.")
print(f"{name.upper():>20} is right-aligned in a field of width 20.")
print(f"{age:.2f} is formatted to two decimal places.")


# Functions
def greet_user(username):
    """Function to greet a user by their name."""
    print(f"Hello, {username}! Welcome to Python programming.")


greet_user("Nitin")


def add_numbers(a, b):
    """Function to add two numbers and return the result."""
    return a + b


result = add_numbers(5, 10)
print(f"The sum of 5 and 10 is: {result}")
