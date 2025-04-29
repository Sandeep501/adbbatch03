# functions/methods

# def addition():
#     return "somethign"

# def addition(a, b):
#     return a + b

# print(addition(10, 30))
# print(addition(100, 300))

# find the squares

# n = int(input())

# def find_squares(x):
#     for i in range(x):
#         print(i**2)

# find_squares(n)

# ----------------------------------

# def outer(x):
#     def inner(y):
#         return x + y
#     return inner

# add_num = outer(5)
# print(add_num(10))

# -------------------------------------

# lambda functions

# def multiplication(a, b):
#     return a * b

multiplication = lambda a, b: a * b
# print(multiplication(10, 20))


# def is_even(a):
#     if a % 2 == 0:
#         return True
#     else:
#         False
        
is_even = lambda a: f"{a} is an even num" if a % 2 == 0 else f"{a} is an odd num"
# print(is_even(31))

data = [10, 20, 30, 45, 55, 65]

evens = list(filter(lambda x: x % 2 == 0, data))
# print(squares)

squares = list(map(lambda x: x**2, evens))
# print(squares)

def count_up_to(max_num):
    cnt = 1
    while cnt <= max_num:
        yield cnt
        cnt += 1
        
# for number in count_up_to(5):
#     print(number)
# n = count_up_to(5)
# print(next(n))
# print(next(n))
# print(next(n))

# ---------------------------------

# list comprehensions

def even_nums():
    c = []
    for i in range(2, 31):
        if i % 2 == 0:
            c.append(i)
    return c
# print(even_nums())

even_nums2 = [i for i in range(2, 31) if i % 2 == 0]
# print(even_nums2)

# even_nums3 = [lambda x: x*x for x in range(2, 31)]
# # print(even_nums3)
# for f in even_nums3:
#     print(f())