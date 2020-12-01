
def dearProfx(m="Sorry prof, but the cat erased half of my journal!\n"):
    def deco(fn):
        def inner(*args, **kwargs):
            print(m)
            return fn(*args, **kwargs)
        return inner
    return deco


def dearProf(fn):
    def inner(*args, **kwargs):
        print("Hello Mr. JA, I hope you like my code ...\n")
        return fn(*args, **kwargs)
    return inner