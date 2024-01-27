"""
's3ooOOooDy' has exams. He wants to study hard this time. He has an array of studying hours per day for the previous exams. He wants to know the length of the maximum non-decreasing contiguous subarray of the studying days, to study as much before his current exams.

Example:

For a = [2,2,1,3,4,1] the answer is 3.

[input] array.integer a

The number of hours he studied each day.

[output] integer

The length of the maximum non-decreasing contiguous subarray.
"""


def studying_hours(a):
    days = 0
    study_hours = a[0]
    subbarray = []
    for item in a:
        if item >= study_hours:
            study_hours = item
            days+=1
        else:
            subbarray.append(days)
            days = 1
            study_hours = item
    subbarray.append(days)

    return max(subbarray)

a = [2, 2, 1, 3, 4, 1]
print(studying_hours(a))
