def dearProf(m="Mr. JA, I hope you like my code ...\n"):
    def new_line_d(fn):
        def new_line(*args, **kwargs):
            print(m)
            return fn(*args, **kwargs)
        return new_line
    return new_line_d