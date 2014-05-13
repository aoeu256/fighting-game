
intro = {}

def Get(a, b, t):
    global intro
    if b < a:
        a, b = b, a
    try:
        intro[a, b](t)
    except KeyError:
        return None