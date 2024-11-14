"""pythagony interpreter"""
import sys


def stop(exit_code: int) -> None:
    """alias for sys.exit"""
    sys.exit(exit_code)


def run(program: tuple) -> None:
    """run a pythagony tuple
    
    program[0] should be the function names, and program[1] should be 
    the arguments to pass to the functions.
    """
    i = 0
    while True:
        program[0][i](*program[1][i])
        i += 1
