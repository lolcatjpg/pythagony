"""variables"""
a = [
    (
        bool,
        print,
        print,
    )[i](*(
        (greeting := "hey"),
        (greeting, "there"),
        ("world",),
    )[i]) for i in range(3)
]
print(a)
