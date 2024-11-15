"""variables"""
a = [
    (
        bool,
        print,
        print,
    )[i](*(
        (greeting := "hi", ),
        (greeting, "there"),
        ("world",),
    )[i]) for i in range(3)
]
