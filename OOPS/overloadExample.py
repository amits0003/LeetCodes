from typing import overload


@overload
def add(a: int, b: int) -> int:
    ...


@overload
def add(a: int, b: int, c: int) -> int:
    ...


@overload
def add(a: int, b: int, c: int, d: int) -> int:
    ...


def add(*args) -> int:
    return args[0] + args[1] if len(args) == 2 else (args[0] + args[1] + args[2] if len(args) == 3 else (
        args[0] + args[1] + args[2] + args[3] if len(args) == 4 else TypeError("Unsupported number of arguments")))


print(add(1, 2))  # Output: 3
print(add(1, 2, 3))  # Output: 6
print(add(1, 2, 3, 4))
print(add(1, 2, 3, 4, 5))
