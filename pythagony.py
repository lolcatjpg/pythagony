"""pythagony interpreter"""
import sys
from examples.hello_world import a

stop = sys.exit


i = 0
while True:
    a[0][i](*a[1][i])
    i += 1
