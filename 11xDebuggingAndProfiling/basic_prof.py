import cProfile

def calc():
    print(2 == 1 + 1)

cProfile.run('calc()')

'''
This script performs basic profiling

    - It imports the built-in cProfile module
    - Defines a function(calc())
    - Then calls the function with cProfile to see a profile of the
      function's performance.
'''
