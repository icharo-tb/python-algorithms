"""PYTHON RECURSIVE ALGORITHM

Recursion is basically calling the function inside the same function
Easy example would be factorial numbers:
    This is a factorial: 4!, where exclamation means factorial of the number 4
        This can be translated to: 4 * 3 * 2 * 1 which is equal to 24
        Also, this problem can be seen as 4 * 3!, and 3 can be seen as 3 * 2! and on and on
        Important: factorial for 1 and 0 are the following (ALWAYS!!)
            - 1! = 1
            - 0! = 1

In the iterative function code what we want to do is an iterative loop that does the following:

        def factorial(4):
            factorial = 1
            for x = 1 to 4:
                factorial = factorial * x
    
    So our code sets a factorial to 1, and its going to loop and multiply x by our number

    Whereas on using recursion, our code will complete factorial of 1! until the number we asked for
        So the code is basically reading and returning until it completes the loop
    So, for a recursive algorithm it would look like this:

        def factorial(n):
            if n < 2:
                return 1
            else:
                return n * factorial(n - 1)
    
    The first condition is our debugging line, in case n is less than 2 just return 1 cause that is the result of factorial for 1 and 0
    Otherwise, return n and multiply it by (n - 1) times
        This works by the logic that, if n = 5 we are gonna multiply it by 4 as 5! is the same as 5 * 4!
            And here is where the loop starts as it will do:
                5 * 4!
                    4 * 3!
                        3 * 2!
                            2 * 1!
                                1 * 0!
                                    -- And then it will return the result (120 in this case) --
"""

# CODE

def recursive_factorial(n):
    if n < 2:
        return 1
    elif n < 0:
        return -1
    else:
        return n * recursive_factorial(n-1)

def iterative_factorial(n):
    if n < 0:
        return -1
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        return factorial    