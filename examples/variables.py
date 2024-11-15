"""variables"""
v = {}
a = [
    (
        v.update,
        print,
        print,
    )[i](*(
        (0, "hey"),
        (v[0], "there"),
        ("world",),
    )[i]) for i in range(3)
]
print(a)
