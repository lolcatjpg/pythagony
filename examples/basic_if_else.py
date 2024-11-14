"""hello world"""
a = [
    (
        print,
        print,
    )[i](*(
        ("hello", "there") if 2 + 2 == 4 else ("hi", "there"),
        ("world",),
    )[i]) for i in range(2)
]
