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
