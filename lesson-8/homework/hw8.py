try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
ValueError:


try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: That's not a valid integer!")
FileNotFoundError:

try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
    print("Error: The file was not found!")
TypeError (Non-numeric input):


try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    result = int(num1) + int(num2)
except TypeError:
    print("Error: Both inputs must be numeric!")
except ValueError:
    print("Error: Invalid input. Please enter numbers!")
PermissionError:


try:
    file = open('restricted_file.txt', 'r')
except PermissionError:
    print("Error: You don't have permission to access this file!")
IndexError:


try:
    my_list = [1, 2, 3]
    print(my_list[5])  # Index out of range
except IndexError:
    print("Error: Index out of range!")
KeyboardInterrupt:

try:
    num = int(input("Enter a number: "))
except KeyboardInterrupt:
    print("\nInput was interrupted!")
ArithmeticError:


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except ArithmeticError:
    print("Error: An arithmetic error occurred!")
UnicodeDecodeError:


try:
    with open('non_utf8_file.txt', 'r', encoding='utf-8') as file:
        content = file.read()
except UnicodeDecodeError:
    print("Error: There is an encoding issue with the file!")
AttributeError:


try:
    my_list = [1, 2, 3]
    my_list.append(4)
    my_list.add(5)  # Incorrect method
except AttributeError:
    print("Error: The attribute does not exist!")
File Input/Output Exercises
Read entire text file:


with open('file.txt', 'r') as file:
    content = file.read()
    print(content)
Read first n lines of a file:


n = int(input("Enter the number of lines: "))
with open('file.txt', 'r') as file:
    for _ in range(n):
        print(file.readline().strip())
Append text to a file:


with open('file.txt', 'a') as file:
    file.write("\nAppended text.")
Read last n lines of a file:


n = int(input("Enter the number of lines: "))
with open('file.txt', 'r') as file:
    lines = file.readlines()
    print(''.join(lines[-n:]))
Read file line by line into a list:


with open('file.txt', 'r') as file:
    lines = file.readlines()
print(lines)
Read file line by line into a variable:


with open('file.txt', 'r') as file:
    content = ""
    for line in file:
        content += line
print(content)
Read file line by line into an array:


with open('file.txt', 'r') as file:
    lines = np.array(file.readlines())
print(lines)
Find the longest words:


with open('file.txt', 'r') as file:
    words = file.read().split()
    longest_words = sorted(words, key=len, reverse=True)
    print(longest_words[:5])  # Top 5 longest words
Count the number of lines:


with open('file.txt', 'r') as file:
    line_count = sum(1 for line in file)
print(f"Number of lines: {line_count}")
Count the frequency of words:


from collections import Counter
with open('file.txt', 'r') as file:
    words = file.read().split()
    word_count = Counter(words)
print(word_count)
Get file size:


import os
file_size = os.path.getsize('file.txt')
print(f"File size: {file_size} bytes")
Write a list to a file:


my_list = ['Apple', 'Banana', 'Cherry']
with open('file.txt', 'w') as file:
    for item in my_list:
        file.write(item + '\n')
Copy contents of a file to another file:


with open('source.txt', 'r') as source_file:
    content = source_file.read()
with open('destination.txt', 'w') as dest_file:
    dest_file.write(content)
Combine each line from the first file with the second:


with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    combined_lines = [line1.strip() + " " + line2.strip() for line1, line2 in zip(lines1, lines2)]
print("\n".join(combined_lines))
Read a random line from a file:


with open('file.txt', 'r') as file:
    lines = file.readlines()
    random_line = random.choice(lines)
print(random_line)
Check if file is closed:


with open('file.txt', 'r') as file:
    print(f"Is file closed? {file.closed}")
Remove newline characters from a file:


with open('file.txt', 'r') as file:
    content = file.read().replace('\n', '')
print(content)
Count words in a file:


with open('file.txt', 'r') as file:
    content = file.read()
    words = content.replace(',', ' ').split()
print(f"Word count: {len(words)}")
Extract characters and store in a list:


with open('file.txt', 'r') as file:
    content = file.read()
    characters = list(content)
print(characters)
Generate 26 text files:


import string
for letter in string.ascii_uppercase:
    with open(f'{letter}.txt', 'w') as file:
        file.write(f"This is file {letter}")
Create file with alphabet letters on each line:


with open('alphabet.txt', 'w') as file:
    for i in range(0, 26, 5):  # Grouping 5 letters per line
        file.write(' '.join(string.ascii_uppercase[i:i+5]) + '\n')
