"""hello world!"""
# add parent dir to path
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


import legacy.pythagony as pa


pa.run((
    (
        print,
        print,
		pa.stop,
    ),
    (
		("hello", "world!", ),
        (f"{1 + 1 = }!", ),
		(0, ),
	)
))
