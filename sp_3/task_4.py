"""
Create function-generator divisor that should return all divisors of the positive number.
If there are no divisors left function should return None.
three = divisor(3)
next(three) => 1
next(three) => 3
next(three) => None
"""
def divisor(num):
    for elem in range(1, num+1):
        if num % elem == 0:
            yield elem
    while True:
        yield None

three = divisor(3)
print(next(three))
print(next(three))
print(next(three))
print(next(three))