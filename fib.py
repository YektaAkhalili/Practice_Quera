#Written by Yekta A Khalili
#May 2019
#Practice Question for Quera exams

"""
Question is :

Given an input number "n", print out a series of +'s and -'s
in a way that the i'th place is a + only if i is in the Fibonacci sequence


"""


n = int(input("Give me an int number between 1 and 100"))

def check_fib(n):
    """checks to see if a number is in the Fibonacci sequence"""
    fib = [1,1,2]
    for i in range(3, 100):
        fib.append(fib[i-1] + fib[i-2])

    if n in fib:
        return True

for i in range(1,n + 1):
    if check_fib(i):
        print("+", end = '')
    else:
        print("-", end= '')
