from asm import Deserializer, Serializer


def foo(a, b, c):
    print('ah')
    if a:
        return foo(1, 2, 3)
    else:
        return foo({}, sum([]), foo)


if __name__ == "__main__":
    d = Deserializer(foo.__code__)
    ops = d.deserialize()
    print(ops)
    s = Serializer(ops, foo.__code__)
    foo.__code__ = s.serialize()
