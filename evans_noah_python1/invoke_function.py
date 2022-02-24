import imp

from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values, or arguments, for each of the function’s parameters.
Functions allow you to write code efficiently. When you need to perform an action more than once, wrap that code in a function and call it when you need it. When you need to change how the action is carried out, you can change the code in the function, and the improvement is applied everywhere.
'''

print("Invoking zero arg function")
zero_arg_function()

print("Invoking function with required arguments")
introduction("Harry", "Houdini")

print("Invoking function with default arguments")
introduction_with_default_args()

#TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file

print("Invoking function with mix of default arguments")
introduction_with_mix_of_default_args('Robert')

print("Invoking function that prints the product of two numbers")
product_of_two_num(10, 1000000)
million_times_ten= product_of_two_num(10, 1000000)
print(str(million_times_ten) + '\n')

print("Invoking function that adds all values in the argument")
print(str(add_all_nums(10, 10, 10, 10, 10, 10, 10, 10, 10, 10))+ '\n')

print('Invoking lambda function that doubles the value in argument')
print(str(double(1000))+ '\n')

print('Invoking a recursive function that returns a Fibonacci sequence')
print(fib(12))

print('\n Invoking function that subtracts two values with local variables')
print(subtract(13, 3))

print('\nInvoking function that tests palindrome status with use of local variables')
print(palindrome_test('civic'))
