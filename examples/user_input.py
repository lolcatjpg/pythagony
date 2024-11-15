"""take user input"""
a = (
    [
        ask := lambda q: result := input(q)
    ],
    [
        (
            print,
            print,
            ask,
        )[i](*(
            ("e", ),
            ("o", result),
            ("a", ),
        )[i]) for i in range(2, -1, -1)
    ]
)
