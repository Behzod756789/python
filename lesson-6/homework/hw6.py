def insert_underscore(txt):
    result = ""
    count = 0
    i = 0
    vowels = 'aeiouAEIOU'

    while i < len(txt):
        result += txt[i]
        count += 1

        if count == 3:
            if txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == '_'):
                pass  # delay underscore
            elif i + 1 < len(txt):
                result += "_"
                count = 0
        i += 1

    print(result)


insert_underscore("hello")         # hel_lo
insert_underscore("assalom")       # ass_alom
insert_underscore("abcabcabcdeabcdefabcdefg")  # abc_abc_abcd_abcd_abcdef



n = int(input())
for i in range(n):
    print(i ** 2)



i = 1
while i <= 10:
    print(i)
    i += 1



for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()



n = int(input("Enter number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum is:", total)



n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n * i)



numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 75 <= num <= 150:
        print(num)




num = input("Enter a number: ")
print("Output:", len(num))





for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()




list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)



for i in range(-10, 0):
    print(i)



for i in range(5):
    print(i)
print("Done!")



for num in range(25, 51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)



a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end="  ")
    a, b = b, a + b





n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! = {fact}")






def uncommon(list1, list2):
    result = []

    for item in list1:
        if list2.count(item) < list1.count(item):
            result.extend([item] * (list1.count(item) - list2.count(item)))

    for item in list2:
        if list1.count(item) < list2.count(item):
            result.extend([item] * (list2.count(item) - list1.count(item)))

    return result

list1 = list(map(int, input("Enter the first list of numbers (space-separated): ").split()))
list2 = list(map(int, input("Enter the second list of numbers (space-separated): ").split()))

print("Uncommon elements:", uncommon(list1, list2))
