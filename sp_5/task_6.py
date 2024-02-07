"""
Write the function sum_slice_array(arr, first, second), which accepts the array (list) 
arr and two numbers (first and second) - the ordinal numbers of the elements of the array that must be added. 
For example, if 3 and 5 were entered, the 3rd and 5th elements must be added.

The function should generate exceptions MyExceptions:
if non-numbers or numbers less than 1 were entered;
if non-numbers obtained from array;
if when one of the numbers or both is larger than the array length.
"""
class MyExceptions(Exception):
    def __init__(self, message):
        self.message = message

def sum_slice_array(arr, first, second):
    try:
        if not isinstance(first, int) or not isinstance(second, int) or first < 1 or second < 1:
            raise MyExceptions("Non-numbers or numbers less than 1 were entered.")
        if first > len(arr) or second > len(arr):
            raise MyExceptions("One or both of the indices are larger than the array length.")
        if not (isinstance(arr[first - 1], (int, float)) and isinstance(arr[second - 1], (int, float))):
            raise MyExceptions("Non-numbers obtained from array.")
        
        return float(arr[first - 1] + arr[second - 1])
    except MyExceptions as err:
        raise err

# Test cases
arr = [1, 2, 'a', 4, 5]
try:
    print(sum_slice_array(arr, 3, 5))  # Output: Raises MyExceptions: Non-numbers obtained from array.
except MyExceptions as e:
    print(e.message)

try:
    print(sum_slice_array(arr, 1, 6))  # Output: Raises MyExceptions: One or both of the indices are larger than the array length.
except MyExceptions as e:
    print(e.message)

try:
    print(sum_slice_array(arr, 'x', 2))  # Output: Raises MyExceptions: Non-numbers or numbers less than 1 were entered.
except MyExceptions as e:
    print(e.message)

try:
    print(sum_slice_array(arr, 1, 2))  # Output: 3.0 (1 + 2 = 3)
except MyExceptions as e:
    print(e.message)
