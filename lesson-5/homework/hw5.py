year = int(input("Enter a year: "))

if not isinstance(year, int):
    raise ValueError("Year must be an integer.")

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("Leap Year:", is_leap)



n = int(input("Enter a number: "))

if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")



a = int(input("Enter a: "))
b = int(input("Enter b: "))

start = a if a % 2 == 0 else a + 1
end = b if b % 2 == 0 else b - 1

evens = list(range(min(start, end), max(start, end)+1, 2)) if a <= b else list(range(min(end, start), max(end, start)+1, 2))
print(evens)



a = int(input("Enter a: "))
b = int(input("Enter b: "))

evens = list(filter(lambda x: x % 2 == 0, range(min(a, b), max(a, b)+1)))
print(evens)
