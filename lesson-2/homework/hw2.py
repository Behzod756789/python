
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
age = 2025 - birth_year
print(f"{name}, you are {age} years old.")

txt1 = 'LMaasleitbtui'
print("Extracted car name 1:", txt1[::2])  # Take every second letter

txt2 = 'MsaatmiazD'
print("Extracted car name 2:", txt2[::2])  # Take every second letter

txt3 = "I'am John. I am from London"
area = txt3.split("from")[-1].strip()
print("Residence area:", area)

text = input("Enter a string to reverse: ")
print("Reversed:", text[::-1])


sentence = input("Enter a string to count vowels: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in sentence if char in vowels)
print("Number of vowels:", vowel_count)

numbers = input("Enter numbers separated by space: ")
num_list = list(map(int, numbers.split()))
print("Maximum value:", max(num_list))

word = input("Enter a word to check palindrome: ")
print(f"{word} is a palindrome." if word == word[::-1] else f"{word} is not a palindrome.")

email = input("Enter your email: ")
domain = email.split('@')[1] if '@' in email else 'Invalid email'
print("Email domain:", domain)

chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(12))
print("Generated password:", password)
