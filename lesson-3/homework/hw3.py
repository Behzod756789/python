fruits = ['apple', 'banana', 'cherry', 'mango', 'grape']
print("Third fruit:", fruits[2])

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated List:", concatenated_list)

numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]
new_list = [first, middle, last]
print("Extracted Elements:", new_list)

favorite_movies = ['Inception', 'Matrix', 'Interstellar', 'Titanic', 'Avengers']
movies_tuple = tuple(favorite_movies)
print("Movies Tuple:", movies_tuple)

cities = ['New York', 'London', 'Paris', 'Tokyo']
is_paris_in_list = "Paris" in cities
print("Is Paris in the list?", is_paris_in_list)

nums = [1, 2, 3]
duplicated_list = nums * 2
print("Duplicated List:", duplicated_list)

swap_list = [10, 20, 30, 40, 50]
swap_list[0], swap_list[-1] = swap_list[-1], swap_list[0]
print("Swapped List:", swap_list)

number_tuple = tuple(range(1, 11))
sliced = number_tuple[3:8]
print("Sliced Tuple (index 3 to 7):", sliced)

colors = ['red', 'blue', 'green', 'blue', 'yellow', 'blue']
blue_count = colors.count('blue')
print("Number of 'blue':", blue_count)

animals = ('cat', 'dog', 'lion', 'tiger')
lion_index = animals.index('lion')
print("Index of 'lion':", lion_index)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("Merged Tuple:", merged_tuple)

sample_list = [1, 2, 3, 4]
sample_tuple = (5, 6, 7)
print("Length of List:", len(sample_list))
print("Length of Tuple:", len(sample_tuple))

tuple_to_convert = (100, 200, 300, 400, 500)
converted_list = list(tuple_to_convert)
print("Converted List:", converted_list)

num_tuple = (9, 3, 7, 1, 5)
print("Maximum:", max(num_tuple))
print("Minimum:", min(num_tuple))

# 15. Reverse a Tuple
words = ('hello', 'world', 'python', 'rocks')
reversed_words = words[::-1]
print("Reversed Tuple:", reversed_words)
