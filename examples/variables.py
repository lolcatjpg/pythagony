"""variables"""
a = [
    (
        bool,  # will just return True if its argument isn't False, this gets ignored
        print,
        print,
    )[i](*(
        (greeting := "hey",),
        (greeting, "there"),
        ("world",),
    )[i]) for i in range(3)
]
