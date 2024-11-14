"""hello world with if"""
# add parent dir to path
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import legacy.pythagony as pa

code = (
    (
        pa.run,
        print,
        None
    ),
    (
        (
            (
                (
                    print,
                    print,
                    None
                ),
                (
                    ("Hello",),
                    ("there",),
                )
            )
            if 1 + 1 == 3 else
            (
                (
                    print,
                    print,
                    None
                ),
                (
                    ("Hi",),
                    ("there",),
                )
            ),
        ),
        ("world!",),
    )
)

pa.run(code)
