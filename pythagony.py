"""pythagony interpreter"""
import sys



def run(program: tuple) -> None:
    """### run a pythagony tuple
    
    _program[0]_ should be the function names, and _program[1]_ should be 
    the arguments to pass to the functions.
    use `None` instead of a function name to stop running the tuple.
    """
    i = 0
    while True:
        if program[0][i] is None:
            break

        program[0][i](*program[1][i])
        i += 1
