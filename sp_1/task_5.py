"""
Convert a certain expression like 2+3 to expression in a postfix notation.

The given expression can have one of the following tokens:

a number;
a parenthesis;
arithmetic operator:
subtraction (-);
addition (+);
multiplication (*);
devision (/);
modulo operation (%).
Example:

For expression = ["2","+","3"] the output should be ["2","3","+"].

[execution time limit] 4 seconds (py)

[input] array.string expression

An array of tokes of a valid expression in the standard notation.

[output] array.string

Tokens of the expression in the postfix notation.
"""

def toPostFixExpression(e):
    stack_elements = []
    expressions = []
    
    for item in e:
        if item.isalnum():
            expressions.append(item)
        elif item == '(':
            stack_elements.append(item)
        elif item == ')':
            top = stack_elements.pop()
            while top != '(':
                expressions.append(top)
                top = stack_elements.pop()
        else:
            stack_elements.append(item)

    while stack_elements:
        expressions.append(stack_elements.pop())
    return expressions


print(toPostFixExpression(["20",
                            "+",
                            "3",
                            "*",
                            "(",
                            "5",
                            "*",
                            "4",
                            ")"]))