"""
Create function create with one string argument. 
This function should return anonymous function that checks 
if the argument of function is equals to the argument of outer function. 

For example: 

 tom = create("pass_for_Tom") 

 tom("pass_for_Tom") returns true 

 tom("pass_for_tom") returns false
"""
def create(test_data):
    return lambda result: result == test_data
