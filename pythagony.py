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


def if_else(conditon: bool, program_if_true: tuple, program_if_false: tuple) -> None:
    """### if else clause
    
    condition: condition to check
    program_if_true: tuple to run if the condition is `True`
    program_if_false: tuple to run if the condition is `False`
    """
    if conditon:
        run(program_if_true)
    else:
        run(program_if_false)
