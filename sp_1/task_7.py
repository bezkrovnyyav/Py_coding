"""
Nicky and Dev work in a company where each member is given his income in the form of points. On Nicky's birthday, Dev decided to give some of his points as a gift. The number of points Dev is gifting is the total number of visible zeros visible in the string representation of the N points he received this month.

Let's say that Nicky got M points from Dev. By the company law, if M is even and greater than 0, Nicky must give one point to the company. If M is odd, the company gives Nicky one additional point.

Given the number of points N Dev received this month, calculate the number of points Nicky will receive as a gift and return this number in its binary form.

Note: visible zeros are calculated as follows:

0, 6 and 9 contain 1 visible zero each;
8 contains 2 visible zeros;
other digits do not contain visible zeros.
Example

For N = "565", the output should be
Cipher_Zeroes(N) = 10.

There's one visible zero in "565". Since one is odd, the company will give an additional point, so Nicky will receive 2 points.
210 = 102, so the output should be 10.

Input/Output

[input] string N

The number of points Dev received this month.

Constraints:
1 ≤ N ≤ 101000.

[output] integer

The number of points Nicky will receive in the binary representation.
"""

def Cipher_Zeroes(N):

    counter = 0

    for elem in N:
        if elem == "0" or elem == "6" or elem == "9":
            counter += 1
        if elem == "8":
            counter += 2

    if counter % 2 == 1:
        counter += 1
    elif counter % 2 == 0 and counter > 0:
        counter -= 1
         
    if not counter:
        return 0
    return bin(counter)[2:]
    

print(Cipher_Zeroes("565"))