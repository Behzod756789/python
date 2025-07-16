my_dict = {'a': 3, 'b': 1, 'c': 2}

sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", sorted_asc)


  sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", sorted_desc)







my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)





dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Using dictionary unpacking (Python 3.5+)
result = {**dic1, **dic2, **dic3}
print(result)





def square(x):
    return x * x

squares = dict(zip(range(1, n+1), map(square, range(1, n+1))))
print(squares)



def square(x):
    return x * x

squares = dict(zip(range(1, 16), map(square, range(1, 16))))
print(squares)


my_set = set([1, 2, 3])
print(my_set)



my_set = set([1, 2, 3])
my_set.add(4)
my_set.update([5, 6])
print(my_set)



my_set = set([1, 2, 3])
my_set.discard(2)  
my_set.remove(1)  
print(my_set)



my_set = set([1, 2, 3])
my_set.discard(3)  # discard handles "if exists"
print(my_set)



  
