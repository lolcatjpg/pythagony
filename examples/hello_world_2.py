"""hello world with if"""
# add parent dir to path
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import pythagony as pa

code = (
    (
        pa.if_else,
        print,
        None
    ),
    (
        (
            2 + 2 == 4,  # try changing this to a false condition
            (
                (
                    print,
                    None
                ),
                (
                    ("Hello",),
                )
            ),
            (
                (
                    print,
                    None
                ),
                (
                    ("Hi",),
                )
            )
        ),
        ("world!",),
    )
)

pa.run(code)
