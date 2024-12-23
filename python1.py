# 1-misol
# def counter():
#     count = 0

#     def inner():
#         nonlocal count
#         count += 1
#         return count

#     return inner

# count_func = counter()
# print(count_func())  
# print(count_func())  
# print(count_func())  

# 2-misol
# def greater_than(threshold):
#     def inner(lst):
#         return [x for x in lst if x > threshold]
#     return inner

# five = greater_than(5)
# one = greater_than(1)

# print(five([2, 4, 6, 1, 8]))  
# print(one([1, 0, 8]))         

# 3-misol
# def math_operations(number, operation):
#     def inner(other_number):
#         if operation == "add":
#             return number + other_number
#         elif operation == "subtract":
#             return number - other_number
#         elif operation == "multiply":
#             return number * other_number
#         elif operation == "divide":
#             if other_number != 0:
#                 return number / other_number
#             else:
#                 return "Cannot divide by zero"
#         else:
#             return "Invalid operation"
#     return inner

# add_five = math_operations(5, "add")
# subtract_five = math_operations(5, "subtract")

# print(add_five(3)) 
# print(subtract_five(3))  

# 4-misol
# def even_numbers(lst):
#     return [x for x in lst if x % 2 == 0]

# def odd_numbers(lst):
#     return [x for x in lst if x % 2 != 0]

# print(even_numbers([2, 3, 8]))  
# print(odd_numbers([2, 3, 8])) 

# 5-misol
# def palindrome_numbers(lst):
#     return [x for x in lst if str(x) == str(x)[::-1]]

# def non_palindrome_numbers(lst):
#     return [x for x in lst if str(x) != str(x)[::-1]]

# print(palindrome_numbers([121, 123, 131, 454]))  
# print(non_palindrome_numbers([121, 123, 131, 454])) 

# 6-misol
# def prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def numbers(lst):
#     return [x for x in lst if prime(x)]

# def non_numbers(lst):
#     return [x for x in lst if not prime(x)]

# print(prime_numbers([2, 3, 4, 5, 6, 7, 8, 9, 10]))  
# print(non_numbers([2, 3, 4, 5, 6, 7, 8, 9, 10]))  