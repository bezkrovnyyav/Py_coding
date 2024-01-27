"""
For the given integer n, consider an increasing sequence consisting of all positive integers that are either powers of n, or sums of distinct powers of n.

Your task is to find the kth (1-based) number in this sequence.

Example

For n = 3 and k = 4, the output should be
kthTerm(n, k) = 9.

For n = 3, the sequence described above begins as follows: 1, 3, 4, 9, 10, 12, 13...
[3**0] => [1]
[1, 3**1, 3**1 +1] => [1, 3, 4]
[1, 3, 4, 3**2, 3**2 +1, 3**2 +3, 3**2 +4] => [1, 3, 4, 9, 10, 12, 13]
...

The 4th number in this sequence is 9, which is the answer.
"""

def kthTerm(n, k):
    num_list = [0, 1]
    counter = 1
    while len(num_list) <= k:
        for item in range(len(num_list)):
            num_list.append(n**counter + num_list[item])
        counter += 1
    return num_list[k]
