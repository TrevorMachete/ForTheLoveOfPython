grades = {
    'Matt': 77,
    'Macs': 85,
    'Stillo': 68,
    'Louis': 45
}

grades_ls = grades.values()
avgs = sum(grades_ls) / len(grades_ls)
print(avgs)

"""
This script stores student grades in a dictionary and calculates their average

- Defines a dictionary with student names and grades.
- Creates an object with the grades from the dictionary as content.
- Uses the sum() function to sum the grades and then, divide them by the
  length of their object to get the average.

Finally, we print the output
"""