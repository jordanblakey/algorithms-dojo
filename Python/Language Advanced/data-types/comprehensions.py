nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic Comprehension
list_comp = [x for x in nums]
print(list_comp)

# Operation on each elem
map_list = map(lambda n: n * n, nums)
print(list(map_list))

# Greater than
list_filter = [x for x in nums if x > 5]
print(list(list_filter))

# Even numbers filter
filter_lambda = filter(lambda n: n % 2 == 0, nums)
print(list(filter_lambda))
print([x for x in nums if x % 2 == 0])


# Nested for
tuple_list = []
for letter in 'abcd':
    for num in range(4):
        tuple_list.append((letter, num))
print(tuple_list)

tuple_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(tuple_list)

# Dictionary from 2 lists
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
zip_dict = {}
for name, hero in zip(names, heros):
    zip_dict[name] = hero
print(zip_dict)

# Using a dictionary comprehension
comp_dict = {name: hero for name, hero in zip(names, heros)}
print(comp_dict)

comp_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(comp_dict)

# Set Comprehensions
nums = [11, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
loop_set = set()
for n in nums:
    loop_set.add(n)
print(loop_set)

comp_set = {n for n in nums}
print(comp_set)


# Generator Comprehensions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Generators

def gen_func(nums):
    for n in nums:
        yield n + n


gen = gen_func(nums)
print(gen)

for x in gen:
    print(x)

gen = (x * x for x in nums)
for x in gen:
    print(x)


def my_range(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


nums = my_range(10, 20)
for num in nums:
    print(num)
